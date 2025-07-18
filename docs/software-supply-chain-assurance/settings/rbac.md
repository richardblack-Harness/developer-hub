---
title: RBAC
description: Manage SCS Roles and Permissions with RBAC.
sidebar_position: 90

redirect_from:
  - /docs/software-supply-chain-assurance/ssca-access-control
---

# Manage SCS Access Control

Harness's RBAC system enables you to precisely manage the user access to specific features or resources and the scope of actions they are permitted to perform. To delve deeper into the specifics of RBAC within Harness, refer to the documentation on [Role-based Access Control (RBAC)](https://developer.harness.io/docs/platform/role-based-access-control/rbac-in-harness/).


## RBAC for Remediation Tracker

The configuration of RBAC for the Remediation Tracker is possible at three levels: Account, [Organization](/docs/software-supply-chain-assurance/settings/rbac#organization), and [Project](/docs/software-supply-chain-assurance/settings/rbac#project).

### Creating and Managing Roles

Here's a guide to creating a role or managing permissions for the Remediation Tracker at the account level:



1. Navigate to **Account Settings** > **Access Control** > **Roles** within your Harness Account.


<DocImage path={require('./static/sca-access-control.png')} width="100%" height="80%" title="Click to view full size image" />

2. Add a new role or select an existing one to modify.


<DocImage path={require('./static/access-control-rbac.png')} width="100%" height="80%" title="Click to view full size image" />


3. Within the role, select Supply Chain Assurance. This action will display the SCS Permissions.


<DocImage path={require('./static/access-control-permissions.png')} width="100%" height="80%" title="Click to view full size image" />
The Remediation Tracker is governed by the following permissions:



* **View**: Grants users the ability to view trackers in a read-only mode.
* **Create/Edit**: Enables users to create new trackers and edit existing ones.
* **Close:** Allows users to close any trackers.


#### **Organization**: 

To configure roles and permissions at the organization level, open the Organization Settings. From the module navigation bar, select your desired organization, then choose **Access Control**. Here, you can configure the roles and permissions at the organization level, following a process similar to the one used at the account level

#### **Project**: 
To set roles and permissions at the Project level, open the Project Settings, and select **Access Control**. Follow similar steps as above to establish the roles and permissions for the project level.

### Creating and Managing Resource Groups

Here's how you can create and manage resource groups for the remediation tracker at the account level. Additionally, you can refer to [Manage Resource Groups](https://developer.harness.io/docs/platform/role-based-access-control/add-resource-groups/) document to learn more.

1. Navigate to **Account Settings** > **Access Control** > **Resource groups** within your Harness Account.
2. Add a new resource group or select an existing one to modify.
3. Set the "Resource Scope" accordingly if you are creating one.
4. Within the Resources, select Supply Chain Assurance.


<DocImage path={require('./static/access-control-remediation.png')} width="100%" height="80%" title="Click to view full size image" />

For configuring at both the organization and project levels, the navigation process is similar to what was detailed in the previous section.