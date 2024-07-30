import requests

# Define the endpoints and the markdown file path
terraform_endpoint = "https://app.harness.io/gateway/iacm/api/provisioners/supported/terraform"
opentofu_endpoint = "https://app.harness.io/gateway/iacm/api/provisioners/supported/opentofu"
markdown_file_path = "docs/infra-as-code-management/whats-supported.md"

# Replace 'your_api_token_here' with your actual API token
api_token = 'pat.l7HREAyVTnyfUsfUtPZUow.66a7bc9a9ab8b07b81bfff24.oPr4rIpBqLEUcaaDo3YB'

# Function to fetch the latest version from a given endpoint with authentication
def fetch_latest_version(url):
    headers = {
        'x-api-key': f'{api_token}',
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        versions = response.json()
        return versions[-1]  # Get the last item from the list
    else:
        raise Exception(f"Failed to fetch versions from {url}. Status code: {response.status_code}")

try:
    # Fetch the latest versions
    latest_terraform_version = fetch_latest_version(terraform_endpoint)
    latest_opentofu_version = fetch_latest_version(opentofu_endpoint)

    # Update the markdown file
    with open(markdown_file_path, "r") as file:
        content = file.read()

    # Define the new lines to replace the placeholders
    terraform_line = f"**Terraform** (up to version {latest_terraform_version})"
    opentofu_line = f"**OpenTofu** (up to version {latest_opentofu_version})"

    terraform_placeholder = "<!-- TERRAFORM_VERSION_PLACEHOLDER -->"
    opentofu_placeholder = "<!-- OPENTOFU_VERSION_PLACEHOLDER -->"

    # Replace the placeholders with the new lines
    updated_content = content.replace(terraform_placeholder, terraform_line)
    updated_content = updated_content.replace(opentofu_placeholder, opentofu_line)

    # Write the updated content back to the markdown file
    with open(markdown_file_path, "w") as file:
        file.write(updated_content)
    print("Markdown file updated successfully.")
except Exception as e:
    print(str(e))