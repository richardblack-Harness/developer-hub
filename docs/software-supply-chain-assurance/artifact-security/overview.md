---
title: Artifact Overview
description: Track the deployment of your open-source components
sidebar_position: 1

redirect_from:

- /docs/software-supply-chain-assurance/artifact-view
---

The **Artifacts** section in the SCS module is a centralized hub for viewing all your container images and their details, providing deeper visibility into your artifacts from multiple perspectives within the software supply chain. Here are the key features this section offers:



* **[Artifact Listing](#view-your-artifacts):** View all container images, including their digests and tags.
* **[Dependency Visibility](#sbom-tab):** Gain insight into artifact dependencies through SBOM.
* **[Chain of Custody](#chain-of-custody):** Log the artifact's journey throughout the software supply chain.
* **[Policy Enforcement](#artifact-overview):** View SBOM policy violations.
* **[Deployment Tracking](#deployments-tab):** Track artifact deployments across various environments.
* **[Security Insights](#vulnerabilities-tab):** Access information on security vulnerabilities.
* **[SLSA Provenance](#artifact-overview):** View the provenance and verification status of artifacts following the SLSA framework.

Any artifacts that go through [SBOM Orchestration](/docs/software-supply-chain-assurance/open-source-management/generate-sbom-for-repositories), [SBOM Policy Enforcement](/docs/software-supply-chain-assurance/open-source-management/enforce-sbom-policies), or [SLSA Provenance](/docs/software-supply-chain-assurance/artifact-security/slsa/generate-slsa) will be listed here. Additionally, the Artifacts section integrates with the Harness CD (Continuous Deployment) and STO (Security Testing Orchestration) modules, providing details linked to deployments and security scanning results for images.


## View your artifacts

The landing page of the Artifacts section provides a comprehensive list of all artifacts, displaying the following details for each: 

* **Name**: The name of the artifact. 
* **Artifact Type**: The type of the artifact
* **Digests**: The number of digests associated with the artifact.
* **Environments**: The environments where the artifact has been deployed with the count. 
* **Vulnerabilities**: The vulnerabilities identified in the most recent scan of the digest. 

<DocImage path={require('./static/artifacts-overview.png')} width="100%" height="100%" title="Click to view full size image" />


#### Search and filter options

You can search for a specific artifact or apply filters based on dependencies, licenses, and environment types to quickly find the necessary information.


## Digests for your artifact

When you select an artifact, you can view the list of all its digests. For each digest, the following details are available:

* **Tags:** The tags associated with the digest.
* **SBOM and Score:** The Software Bill of Materials (SBOM) and its quality score, with an option to download it.
* **Environment:** The count and types of environments (e.g., prod, pre-prod) where the digest has been deployed.
* **Dependencies:** The total number of dependencies included in the image, as detailed in the SBOM.
* **Policy Violations:** A list of all policy violations, including both allow-list and deny-list violations.
* **Vulnerabilities:** The count of vulnerabilities categorized by severity: Critical, High, Medium, and Low.


<DocImage path={require('./static/artifacts-digest.png')} width="100%" height="100%" title="Click to view full size image" />


#### Search and filter options:

You can search for a specific digest or apply filters based on dependencies, licenses, policy violations, and environment types to quickly find the required data.


## Artifact Overview


<DocImage path={require('./static/scs-fullview.png')} width="100%" height="100%" title="Click to view full size image" />


When you select an artifact’s digest, you can view a complete overview. This tab provides general information about the artifact and summarizes the following aspects concisely:


* **Deployments:** Displays the count of deployments specific to each environment (e.g., prod, pre-prod).
* **SBOM:** Shows the total number of dependencies along with the SBOM score. You can also download the SBOM from here.
* **SBOM Policy Violations:** Lists the SBOM policy violations for both allow-list and deny-list categories.
* **Vulnerabilities:** Provides a summary of vulnerabilities found from the security scan, categorized by severity: critical, high, medium, and low.
* **SLSA:** Shows the status of SLSA verification (passed/failed). You can also download the SLSA provenance from here.
* **Artifact Signing and Verification:** Displays the artifact signing details and verification results, along with a link to view the logs.

### Chain of Custody
The Chain of Custody provides a comprehensive and immutable record of an artifact's lifecycle throughout the software supply chain. It captures every significant event during the artifact's journey, allowing detailed traceability. These logs include events from stages such as **Build** (Harness CI), **Deploy**, and **Security** (actions from the Harness **STO** and **SCS** modules).

Each entry in the Chain of Custody contains relevant details about the artifact's progress, such as the status of the event, any associated downloadable artifacts, or a link to the pipeline execution results for further details. The information recorded varies depending on the specific event and includes:

- **What**: The operation performed on the artifact.  
- **When**: The timestamp of the action.  
- **Where**: The stage where the event occurred.  
- **Why**: The purpose of the action, often linked to pipeline execution data.

<DocImage path={require('./static/scs-chainofcustody.png')} width="100%" height="100%" title="Click to view full size image" />

## SBOM Tab

The SBOM tab presents details of all the dependencies within the artifact, including dependencies from various levels, such as the application level, distribution level, and OS level. With a count of total dependencies at the top, the tab provides the following details:



* **Dependency Name:** Name of the dependency.
* **License:** Name of the dependency’s license.
* **Package Manager:** Tool managing the package.
* **PURL:** Package URL.
* **Supplier:** Source of the dependency.
* **Vulnerabilities:** Provides a summary of vulnerabilities found from the Snyk scan, categorized by severity: critical, high, medium, and low.

<DocImage path={require('./static/component-sbom-for-artifacts.png')} width="100%" height="100%" title="Click to view full size image" />


For more information about the levels of image dependencies, refer to the [How to detect base images in SBOM](/docs/software-supply-chain-assurance/how-to-guides/label-components-from-image) documentation.


#### Search and filter options

You can search for a package manager and supplier or apply filters based on dependencies, licenses, and image layers to quickly find the required data.


## Deployments Tab

The Deployments tab enables you to track the active deployments of your artifact. With a count of active deployments, this tab provides the following details:



* **Environment:** Name and ID of the environment.
* **Type:** Environment type (Prod or Pre-prod).
* **Last Pipeline Execution:** Pipeline that last deployed the artifact.
* **Policy Violations:** Lists SBOM policy violations (allow-list and deny-list).
* **SLSA Verification:** Shows SLSA verification status, including both SLSA policy and attestation verification statuses.
* **Triggered By:** Details about the deployment trigger.


<DocImage path={require('./static/artifacts-deployments.png')} width="100%" height="100%" title="Click to view full size image" />


#### Search and filter options

You can search for an environment or apply filters based on environment type and policy violations to quickly find the required data.

:::note 

Harness SCS provides support for tracking artifact deployments to Kubernetes, Native Helm, and Amazon ECS.

:::

## Vulnerabilities Tab

The Vulnerabilities tab presents the scan results performed on the artifact, consolidating findings from various scanning tools. This view categorizes all identified vulnerabilities by severity and allows filtering based on scanners and other details. The security scanning is facilitated by the Harness STO (Security Testing Orchestration) module.

:::note

To ensure vulnerability results appear on the Artifacts page, run STO scans on images that are pushed to Docker registry.Scanning images locally before publishing will result in a digest mismatch, preventing SCS from linking the vulnerability data.

:::

<DocImage path={require('./static/artifacts-vulnerabilities.png')} width="100%" height="100%" title="Click to view full size image" />

Refer to [view security test results](/docs/security-testing-orchestration/view-security-test-results/view-scan-results) in Harness STO documentation for more detailed information about the view and navigation.
