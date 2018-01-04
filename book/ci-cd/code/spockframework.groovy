// source: http://thejavatar.com/testing-with-spock/

def "should return false if user does not have role required for viewing page"() {
   given:
      // context
      pageRequiresRole Role.ADMIN
      userHasRole Role.USER
   when:
      // some action is performed
      boolean authorized = authorizationService.isUserAuthorizedForPage(user, page)
   then:
      // expect specific result
      authorized == false
}
