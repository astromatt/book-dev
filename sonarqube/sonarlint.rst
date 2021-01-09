*********
SonarLint
*********


Rationale
=========
SonarLint is an IDE extension that helps you detect and fix quality issues as you write code.
Like a spell checker, SonarLint squiggles flaws so that they can be fixed before committing code. [officialpage]_

.. figure:: _img/sonarqube-bigpicture.png

.. image:: _img/sonarlint-a.jpg
    :class: hidden

.. image:: _img/sonarlint-b.mp4
    :class: hidden

.. raw:: html

    <video autoplay="" loop="" muted="" playsinline="" src="../_images/sonarlint-b.mp4" poster="../_images/sonarlint-a.jpg" width="100%" height="100%" alt="SonarLint is an IDE extension that helps you detect and fix quality issues as you write code. [officialpage]_"></video>


Supports
========
* Jetbrains IDE:

    * InteliJ IDEA
    * PyCharm
    * PHPStorm
    * Webstorm
    * Rubymine
    * ...

* Eclipse
* Visual Studio
* VS Code


Roadmap
=======
Here are some of the big topics that are on our mind at SonarSource, on top of continuously improving the user experience and refining features so that SonarLint always helps you fix issues before they exist.

**Focus on rules and issues that matter**
Out-of-the-box, we want SonarLint to remain as simple and powerful as possible, so that you can focus on your coding. In the same spirit, if you think there are a few coding rules or issues that do not apply to your specific case, then we want you to be in control and use SonarLint to its full extent, to avoid any disturbance. That includes:

    * excluding specific files from SonarLint analysis
    * deactivating specific rules that are not valuable to you
    * muting specific issues that you deem as not-applicable
    * enabling non-default rules that you would like to be checked as you code

This should be available to all developers across all IDEs supported by SonarLint.

**Feature parity, across all IDEs**
VSCode is the youngest member of the SonarLint-supported family. As such, SonarLint for VSCode may not offer all the features and capabilities it provides in other IDEs, however the end goal is feature parity with the other SonarLint members! We really want all developers, irrespective of the language and IDE they code in, to benefit from the full feature-set of SonarLint.

**End-to-end experience for SonarQube and SonarCloud users**
SonarLint Connected Mode unlocks integrations with SonarQube/ SonarCloud, so that the issues reported in your IDE are in line with the project health and Quality Gate that your team is tracking. As more features make it to SonarQube/SonarCloud, we want to make sure they are also integrated with SonarLint whenever it provides value. For example, just think of SonarLint detecting the branch you’re working on, and aligning its code analysis with what is reported in SonarQube/SonarCloud (now supporting branch and PR analysis).

**Continuous language updates**
The SonarSource Language Team is continuously advancing its in-house bug and vulnerability detection engine. Across all programming languages and across all IDEs, you can expect recurring additions of new static analysis rules and even new languages based on interest and relevance! Make sure to get the big picture @ rules.sonarsource.com.



References
==========
.. [officialpage] https://www.sonarlint.org
