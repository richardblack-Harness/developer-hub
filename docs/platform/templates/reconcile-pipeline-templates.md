---
title: Reconcile pipeline template changes
description: This topic explains how to reconcile pipeline template changes in Harness.
sidebar_position: 15
canonical_url: https://www.harness.io/blog/ci-cd-pipeline-as-code-with-harness
---

If any [entity](https://developer.harness.io/docs/platform/references/harness-entity-reference/) referenced in a pipeline is updated, Harness prompts you to update the pipeline if you're viewing the pipeline in Pipeline Studio. Harness detects updates made to the referenced entities using Pipeline Studio or YAML view. 

This process of updating the referenced entities in the pipeline is called pipeline reconciliation. It ensures that you are aware that referenced entities have updates and you can choose to integrate those changes into the pipeline. 

One of the most common example of pipeline reconciliation is when you increase or decrease the number of runtime inputs.

Let's consider a scenario with three templates: a pipeline template, a stage template, and a step template. In this scenario, the pipeline serves as the parent template, the stage is the pipeline's child template, and the step is the stage's child template.

**Step Template**
```yaml
template:
  name: step_template_1
  identifier: step_template_1
  versionLabel: v1
  type: Step
  projectIdentifier: Pipeline_Samples
  orgIdentifier: default1
  tags: {}
  spec:
    timeout: 10m
    type: ShellScript
    spec:
      shell: Bash
      executionTarget: {}
      delegateSelectors: []
      source:
        type: Inline
        spec:
          script: echo hello
      environmentVariables:
        - name: var1
          type: String
          value: val1
      outputVariables: []

```

**Stage Template**
```yaml
template:
  name: stage_template_1
  identifier: stage_template_1
  versionLabel: v1
  type: Stage
  projectIdentifier: Pipeline_Samples
  orgIdentifier: default
  tags: {}
  spec:
    type: Custom
    spec:
      execution:
        steps:
          - step:
              name: steptemp1
              identifier: steptemp1
              template:
                templateRef: step_template_1
                versionLabel: v1

```

**Pipeline Template**
```yaml
template:
  name: pipeline_template_1
  identifier: pipeline_template_1
  versionLabel: v1
  type: Pipeline
  projectIdentifier: Pipeline_Samples
  orgIdentifier: default
  tags: {}
  spec:
    stages:
      - stage:
          name: stagetemp1
          identifier: stagetemp1
          tags: {}
          template:
            templateRef: stage_template_1
            versionLabel: v1

```
In this pipeline template, both step and stage templates are utilized. In this example, when you update a variable at a step level, you changed the value of variable from ``Fixed value`` to ``Runtime input``.

**Step template**
```yaml
template:
  name: step_template_1
  identifier: step_template_1
  versionLabel: v1
  type: Step
  projectIdentifier: Pipeline_Samples
  orgIdentifier: default
  tags: {}
  spec:
    timeout: 10m
    type: ShellScript
    spec:
      shell: Bash
      executionTarget: {}
      delegateSelectors: []
      source:
        type: Inline
        spec:
          script: echo hello
      environmentVariables:
        - name: var1
          type: String
          value: <+input>
      outputVariables: []
```

When you update a child entity, the step template and the parent entities, i.e., stage and pipeline templates must be updated as well. In this scenario, the concept of reconciliation comes into play. 


When you move to the pipeline template, you can see the message: ``Some of the entities referenced in this template have gone out of sync.`` along with a ``Reconcile`` button.
![](./static/reconcile_popup.png)

Harness calls the refreshed YAML API `POST https://app.harness.io/template/api/refresh-template/refreshed-yaml` when you select the **Reconcile** option in **Pipeline Studio**. This API gets the latest pipeline YAML. Harness shows the difference between the original and the refreshed YAML in the UI on the Template Error Inspection page.

![](./static/reconcile_pipeline_template.png)

First, you will be asked to update the stage template, and then the pipeline template. You also have the option to ``Update all unsynced entities`` at once.
:::info note
Every reconciliation requires saving the pipeline. Specifically, if the pipeline is remote, you must to do a ``git push`` every time to ensure that the latest version of the pipeline is saved.
:::

Pipeline reconciliation allows you to add or remove ``allowed values`` to your runtime inputs. However, if you add new allowed values to the parent entity, it will not allow the same. Parent entity can have subset of allowed values that are present in child entity.

For example, You have a pipeline that uses a stage and step template. 

Step template
```yaml
template:
  name: step_template_1
  identifier: step_template_1
  versionLabel: v1
  type: Step
  projectIdentifier: CD_Samples
  orgIdentifier: default
  tags: {}
  spec:
    timeout: 10m
    type: ShellScript
    spec:
      shell: Bash
      executionTarget: {}
      delegateSelectors: []
      source:
        type: Inline
        spec:
          script: echo hello
      environmentVariables:
        - name: var1
          type: String
          value: <+input>.allowedValues(a,b,c,d)
      outputVariables: []

```

The parent entities like stage or pipeline can have subsets of the above mentioned ``allowed values``. But, if you add a new value, for example,``e`` in the parent entity, then it won't allow you to add the same since the child entity in the step template doesn't have that updated value in it's allowed value. The parent entity in the above scenario picks up allowed values from the child entity. 

## How Harness detects changes

Harness APIs detect pipeline template changes that require reconciliation. Harness warns you in the UI when a pipeline references a template with updated entities you must reconcile.

![](./static/entities-require-reconcile.png)

Harness calls the Validate template inputs API `GET https://app.harness.io/pipeline/api/refresh-template/validate-template-inputs` when you select the **Reconcile** option in the **Pipeline Studio**. For more information, go to [Validate template inputs](https://apidocs.harness.io/tag/Pipeline-Refresh#operation/validateTemplateInputs) in the API documentation.

When you save pipeline changes, the Validate pipeline API `POST https://app.harness.io/pipeline/api/pipelines/{pipelineIdentifier}/validate` starts an asynchronous pipeline validation. The same flow is also executed when you view a pipeline (by making a GET call from the Pipelines list page). The YAML is fetched from the cache, so the results may not be the latest.

Harness fetches the response of the validation event from the Get Pipeline validation event data API `GET https://app.harness.io/pipeline/api/pipelines/validate/{uuid}`. This API includes the information to determine whether reconciliation is required.


## What changes are shown

When reconciling a pipeline, Harness shows you the diff between the current YAML configuration and the updated YAML configuration. 

The diff shows only those changes that involve runtime inputs. The following list illustrates the updates that Harness highlights in the diff:

- A field requiring a runtime input was added. This includes scenarios in which the referenced entity was updated to reference another entity, and this change introduced runtime inputs to the configuration (for example, a referenced service was updated to use an artifact source template, and the source template requires runtime inputs). 

  The converse is true: a field requiring a runtime input is removed, either directly or by the removal of a referenced entity such as the artifact source template in the previous example.

- A field's value type was changed from a fixed value or expression to a runtime input, or from a runtime input to a fixed value or expression.


## Resolve conflicts in the pipeline YAML

Harness warns you when a pipeline references a template that needs to be reconciled when you change it.

To resolve conflicts in the pipeline YAML, do the following:

1. In the **Pipeline Studio**, select **Reconcile**. The Template Error Inspection page opens.

   You can view the Git YAML differences for the pipeline and see which lines have been modified. The differences are calculated based on the data, not exact string matches. Therefore, a different quote symbol, such as, `"` versus `'` for the same value might not be recognized as a difference. This is not an issue or error.

2. Update the YAML with the required changes.

3. Select **Save**. Harness reconciles the change, making it the default state.
 
   Harness calls the update pipeline API `PUT https://app.harness.io/pipeline/api/pipelines/{pipelineIdentifier}`, and saves the updated YAML.

## Bulk Reconciliation of templates

:::info note
Currently this feature is behind feature flag `PIPE_BULK_RECONCILIATION`. Please contact [Harness Support](mailto:support@harness.io) to enable this feature flag.
:::

 When changes are made to the runtime inputs in a template—such as adding or removing inputs—and the template is referenced by multiple entities (like other templates, stages, or pipelines), you can trigger a **Bulk Reconciliation** directly from the template page. This process ensures that all dependent entities are synchronized with the updated template in a single operation.

For example you have a step template:-

```yaml
template:
  name: ReconcileStepTemplate
  identifier: ReconcileStepTemplate
  versionLabel: v1
  type: Step
  projectIdentifier: ShivamTemplate
  orgIdentifier: default
  tags: {}
  spec:
    timeout: <+input>
    type: ShellScript
    spec:
      shell: Bash
      executionTarget: {}
      delegateSelectors: []
      source:
        type: Inline
        spec:
          script: <+input>
      environmentVariables:
        - name: var1
          type: String
          value: <+input>
      outputVariables: []
      includeInfraSelectors: <+input>
```


In this example, when you update a variable at a step level, you changed the value of ShellScript from `Runtime input` to `Fixed value`.

```yaml
template:
  name: ReconcileStepTemplate
  identifier: ReconcileStepTemplate
  versionLabel: v1
  type: Step
  projectIdentifier: Testemplate
  orgIdentifier: default
  tags: {}
  spec:
    timeout: <+input>
    type: ShellScript
    spec:
      shell: Bash
      executionTarget: {}
      delegateSelectors: []
      source:
        type: Inline
        spec:
          script: echo hello
      environmentVariables:
        - name: var1
          type: String
          value: <+input>
      outputVariables: []
      includeInfraSelectors: <+input>
```

After saving the template, click on the three dots and select **Reconcile References**.

![](./static/reconcile_references.png)

When you select **Reconcile References**, a list of all entities consuming that step template appears:

![](./static/reconcile_references_update.png)

You can select the entities and click on **Update All Unsynced Entities** to synchronize them with the updated template.

To view the reconciliation status, click on **Reference Reconciliation History**.

![](./static/reference_reconciliation_history.png)

Here, you can view the **Details, Status, Start Time** of each reconciliation.


![](./static/reference_history_details.png)

Clicking on **Details** will show the individual status of each reconciled entity.

![](./static/reconcile_reconciliation_status.png)

:::info note
Important Points for Bulk Reconciliation
- Only inline entities and direct references to templates are supported.
- The user triggering the bulk reconciliation must have **Pipeline Edit** permissions for the entities being updated.
- The username of the individual who triggered the bulk reconciliation will appear in audit logs for update events.
- You can select up to 25 entities in a single bulk reconciliation.
:::

## Understanding Bulk Reconciliation for Remote Entities

:::info note
Currently, this feature is behind the feature flag `PIPE_BULK_RECONCILIATION_PHASE2`. Please contact [Harness Support](mailto:support@harness.io) to enable this feature flag.
:::

### Scenario

You have a Remote Step Template defined as follows:
```yaml
template:
  name: step_test
  identifier: step_test
  versionLabel: v1
  type: Step
  projectIdentifier: test
  orgIdentifier: default
  tags: {}
  spec:
    timeout: 10s
    type: ShellScript
    spec:
      shell: Bash
      executionTarget: {}
      delegateSelectors: []
      source:
        type: Inline
        spec:
          script: echo hello
      environmentVariables: []
      outputVariables: []
```
This Step Template is referenced in a Remote Stage Template:

```yaml
template:
  name: stage_test
  identifier: stage_test
  versionLabel: v1
  type: Stage
  projectIdentifier: Krishika_test_autocreation
  orgIdentifier: default
  tags: {}
  spec:
    type: Custom
    spec:
      execution:
        steps:
          - step:
              name: step1
              identifier: step1
              template:
                templateRef: step_test
                versionLabel: v1
                templateInputs:
                  type: ShellScript
                  timeout: 10s
```
Now, you make a change in the Step Template — updating the `timeout` field from a fixed value to a runtime input — and commit the update to a new branch:

```yaml
template:
  name: step_test
  identifier: step_test
  versionLabel: v1
  type: Step
  projectIdentifier: test
  orgIdentifier: default
  tags: {}
  spec:
    timeout: <+input>
    type: ShellScript
    spec:
      shell: Bash
      executionTarget: {}
      delegateSelectors: []
      source:
        type: Inline
        spec:
          script: echo hello
      environmentVariables: []
      outputVariables: []
```
### Reconciliation Flow

1. After committing the changes, click on **Referencing Entities**.

![](./static/bulk-remote1.png)

2. The Stage Template that references the updated Step Template will appear as **Out of Sync**.

![](./static/bulk-remote2.png)

3. Select the out-of-sync entity and click **Update**.

4. As the update progresses, the Current Status will change to **In Progress**.

![](./static/bulk-remote3.png)

5. Once the PR is created, the Current Status will change to **Pending PR**.

![](./static/bulk-remote4.png)

6. Click on **Pending PR** to view and open the pull request. Click **View PR** to navigate to the repository and merge it into your default branch, where all entities are stored.

![](./static/bulk-remote5.png)

You can also see the difference between Original and Refreshed entity that shows what changes are made.

7. After merging the PR, the Current Status will change to **Synced**.
![](./static/bulk-remote6.png)

## Best practices

While it is technically possible to run a pipeline without performing reconciliation after a template has been updated, this approach is not recommended. Here are key reasons why reconciliation should always be performed:

- **Always uses the latest template version**: When a pipeline executes, it uses the latest version of the template irrespective of whether you reconciled the pipeline or not.
- **Outdated or missing input values**: If reconciliation is not done, the inputs shown in the Pipeline Run form may be outdated or incomplete. For example:
- Newly added input fields in the updated template won’t appear in the form.
- Some values may be passed as null or retain older values that no longer align with the current template structure.
- **Risk of unexpected behavior**: This can lead to null values or stale data being used in the pipeline run, potentially causing failures or unintended behavior in the step or stage execution.
- **No validation warning during execution**: The pipeline executes without warnings about missing or incompatible inputs, which makes it harder to debug issues caused by outdated templates.


### Recommendation
Always click **Reconcile** when prompted after a template change before executing the pipeline. This ensures:

- The pipeline inputs match the latest template structure.
- Runtime inputs are updated and accurately reflected in the form.
- Execution is predictable and stable.