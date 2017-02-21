# Checkstyle, PMD, JaCoCo, Findbugs and PITest build

## English

- Download repository https://github.com/SonarSource/sonar-examples.git
- Start building projects in `sonar-examples/projects/languages/java`
- Push static code analysis results to `SonarQube`
    - You might want to install `SonarQube` using `puppet module install maestrodev/sonarqube`
- Add `pitest` dependency to `pom.xml` and test project using default mutators

## Polish

- Zaciągnij repozytorium https://github.com/SonarSource/sonar-examples.git
- Zacznij budować różne projekty `sonar-examples/projects/languages/java`
- Wyniki upublicznij w `SonarQube`
    - Do instalacji możesz wykorzystać `puppet module install maestrodev/sonarqube`
- Dodaj w `pom.xml` zależność `pitest` i przetestuj projekt wykorzystując domyślne mutatory
