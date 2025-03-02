# :card_box: Functionality

## Structure

- The Python SDK uses multiple classes, representing the **hierarchical structure of UP42**:
    - **Catalog > Order**
    - **Storage > Asset**
    - **Project > Workflow > Job/JobCollection > JobTask**

- Each class object can **spawn elements of one level below**, e.g.
    - `project = up42.initialize_project()`
    - `workflow = project.create_workflow()`
    - `job = workflow.run_job()`


## Functionality

A quick overview how the different class objects are **created, used and which functionality** they offer. More detail
in the [code reference](up42-reference.md).

!!! example "Available Functionality"
    === "up42"

        {{ docstring_up42 }}
        <br>
        Available functions, see also [**up42 reference**](up42-reference.md):
        {{ format_funcs(funcs_up42) }}

    === "Project"

        {{ docstring_project }}
        <br>
        Available functions, see also [**Project reference**](project-reference.md):
        {{ format_funcs(funcs_project) }}
    
    === "Workflow"

        {{ docstring_workflow }}
        <br>
        Available functions, see also [**Workflow reference**](workflow-reference.md):
        {{ format_funcs(funcs_workflow) }}
        
    === "Job"

        {{ docstring_job }}
        <br>
        Available functions, see also [**Job reference**](job-reference.md):
        {{ format_funcs(funcs_job) }}
        
    === "JobTask"

        {{ docstring_jobtask }}
        <br>
        Available functions, see also [**JobTask reference**](jobtask-reference.md):
        {{ format_funcs(funcs_jobtask) }}
        
    === "JobCollection"

        {{ docstring_jobcollection }}
        <br>
        Available functions, see also [**JobCollection reference**](jobcollection-reference.md):
        {{ format_funcs(funcs_jobcollection) }}
        
    === "Catalog"

        {{ docstring_catalog }}
        <br>
        Available functions, see also [**Catalog reference**](catalog-reference.md):
        {{ format_funcs(funcs_catalog) }}

    === "Storage"

        {{ docstring_storage }}
        <br>
        Available functions, see also [**Storage reference**](storage-reference.md):
        {{ format_funcs(funcs_storage) }}
    
    === "Order"

        {{ docstring_order }}
        <br>
        Available functions, see also [**Order reference**](order-reference.md):
        {{ format_funcs(funcs_order) }}
    
    === "Asset"

        {{ docstring_asset }}
        <br>
        Available functions, see also [**Asset reference**](asset-reference.md): 
        {{ format_funcs(funcs_asset) }}

    === "Webhook"

        {{ docstring_webhooks }}
        <br>
        Available functions, see also [**Webhooks reference**](webhooks-reference.md): 
        {{ format_funcs(funcs_webhook) }}
