---
title: Harness Supply Chain Security (SCS) overview
sidebar_label: Overview
description: Secure your software supply chain with Harness SCS
sidebar_position: 1
---

In today's software development landscape, reliance on open-source components and various DevOps tools has become essential for faster development. While this approach streamlines the development process and accelerates product delivery, it also introduces potential risks to the software supply chain. These risks include security vulnerabilities from the extensive chain of dependencies, which can lead to zero-day exploits, licensing discrepancies, and other attacks. Additionally, while there are various tools involved in the software development process, the tools themselves can also open the door to multiple supply chain attacks. 

<DocImage path={require('./static/ssca-overview.png')} width="100%" height="100%" title="Click to view full size image" />


High-profile breaches, like those experienced by Log4j, SolarWinds and Codecov, have further underscored the importance of software supply chain security. While standard security techniques for detecting vulnerabilities in source code are essential, they don't fully address the risks throughout the supply chain journey,  - from source to distribution.

To address these challenges, the Harness Supply Chain Security (SCS) module is designed to secure the software supply chain, ensuring a layer of security that extends beyond conventional measures.


## Supply Chain Security Objectives

The SCS module focuses on securing the software supply chain from two critical perspectives: dependency attacks and exploits from the DevOps toolchain. It ensures that the software remains secure throughout the entire delivery process by addressing risks from both sides. The SCS module helps you to achieve the following objectives



1. **Risk and Compliance Visibility**: Gain insights into the security posture of code repositories, artifacts, and CI/CD tools concerning risk and compliance standards such as [CIS Benchmarks](https://www.cisecurity.org/benchmark/software-supply-chain-security), [OWASP Top 10 CI/CD Risks](https://owasp.org/www-project-top-10-ci-cd-security-risks/), and [SLSA](https://slsa.dev/).
2. **Intelligent Remediation**: Initiate SLAs and track the remediation of all risk and compliance issues, including the removal of non-compliant open-source dependencies, using SBOMs (Software Bill of Materials).
1. **Governance Policy Enforcement**: Achieve a high level of security by collecting evidence and enforcing supply chain governance policies based on compliance standards and SBOMs.

This comprehensive approach helps organizations maintain a secure and compliant software supply chain, mitigating risks from dependencies and ensuring robust protection against potential attacks from the DevOps toolchain.


## Supply Chain Security Features

To realize the objectives, the SCS module offers the following features:



* [Repository security posture management](/docs/software-supply-chain-assurance/manage-risk-and-compliance/repository-security-posture-management-rspm)
* Comply with security compliance standards
    * [CIS Benchmarks](https://www.cisecurity.org/benchmark/software-supply-chain-security)
    * [OWASP Top 10 CI/CD Risks](https://owasp.org/www-project-top-10-ci-cd-security-risks/)
* [SLSA Build Level 1, Level 2 and Level 3.](https://developer.harness.io/docs/software-supply-chain-assurance/slsa/overview)
* [SBOM generation and management.](/docs/software-supply-chain-assurance/open-source-management/generate-sbom-for-repositories)
* [Govern the usage of open source with SBOM policy enforcement.](/docs/software-supply-chain-assurance/open-source-management/enforce-sbom-policies)
* [Remediate issues related to risk & compliance and zero-day exploits.](/docs/software-supply-chain-assurance/open-source-management/remediation-tracker/overview)

For more information about these features and how SCS integrates with the Harness Platform, go to the [SCS key concepts](/docs/software-supply-chain-assurance/get-started/key-concepts).
