# ACL - biuro + internal + cloud
acl local_access {
  "localhost";
  "10.0.0.0"/8;
  "172.16.0.0"/12;
}

backend default {
  .host = "127.0.0.1";
  .port = "8090";
  .connect_timeout = 600s;
  .first_byte_timeout = 600s;
  .between_bytes_timeout = 600s;
  .max_connections = 150;
}

sub vcl_recv {

  if (req.request == "PURGE" && !client.ip ~ local_access) {
    error 405 "Not allowed.";
  }

  if (req.request == "REFRESH" && client.ip ~ local_access) {
    set req.hash_always_miss = true;
  }

  if (req.url ~ "\.(swf|ico|css|js)$" && req.url !~ "(secure|rest)") {
    return (lookup);
  }

  if (req.url ~ "\.(xml)"){
  return(pipe);
  }

  if (req.url ~ "^/secure/projectavatar" || req.url ~ "^/secure/useravatar") {
#    set beresp.http.Cache-Control = "max-age=330";
#    set beresp.ttl = 330s;
  return (lookup);
  }


  if (req.request == "POST") {
    return (pipe);
    }

  return (pass);
}

sub vcl_fetch {
  unset beresp.http.Server;
  set beresp.http.X-Backend = beresp.backend.name;


   if (req.url ~ "^/secure/projectavatar"|| req.url ~ "^/secure/useravatar") {
    set beresp.http.Cache-Control = "max-age=330";
    set beresp.ttl = 1d;
    return (deliver);
  }

  if (beresp.http.Content-Type ~ "text" && beresp.http.Content-Encoding != "gzip") {
    set beresp.do_gzip = true;
  }

  if (beresp.http.Content-Type ~ "application/json" && beresp.http.Content-Encoding != "gzip") {
    set beresp.do_gzip = true;
  }

  if (beresp.http.Content-Type ~ "application/javascript" && beresp.http.Content-Encoding != "gzip") {
    set beresp.do_gzip = true;
  }

#  if (beresp.http.Pragma ~ "no-cache" || beresp.http.Cache-Control ~ "no-cache" || beresp.http.Cache-Control ~ "private") {
#    return(hit_for_pass);

#  }

# ftpd 2013-05-17 - podmiana
#   if (beresp.http.Cache-Control ~ "max-age") {
  if (beresp.http.Cache-Control ~ "max-age" || beresp.http.Cache-Control ~ "s-maxage") {
# ---
    unset beresp.http.Set-Cookie;
    unset beresp.http.X-AREQUESTID;
    unset beresp.http.X-ASESSIONID;
    unset beresp.http.X-AUSERNAME;
    unset beresp.http.X-Seraph-LoginReason;
    return(deliver);
  }
# ftpd 2013-05-17 - dopisanie
  if (beresp.status == 404) {
    set beresp.http.Cache-Control = "max-age=5";
    set beresp.ttl = 5s;
    set beresp.grace = 5s;
  }
# ---
}

sub vcl_hit {
  if (req.request == "PURGE") {
    purge;
    error 200 "Cache purged";
  }
}

sub vcl_miss {
  if (req.request == "PURGE") {
    error 404 "Not in cache";
  }
}

sub vcl_deliver {
# usun naglowki varnisha/php/nginxa
  remove resp.http.X-Varnish;
  remove resp.http.Via;
  remove resp.http.X-Powered-By;
  remove resp.http.Server;
  set resp.http.X-Hit = "HIT " + obj.hits;
  set resp.http.X-Origin = server.hostname;
}

sub vcl_hash {
  hash_data(req.url);
  return (hash);
}


sub vcl_pipe {
  /* Force the connection to be closed afterwards so subsequent reqs don't use pipe */
  set bereq.http.connection = "close";
}

sub vcl_error {
  synthetic "<html><body><!-- Mediation error --></body></html>";
  return (deliver);
}