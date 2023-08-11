environment=$(echo "$ENVIRONMENT" | tr '[:upper:]' '[:lower:]')

config_file=".ci/${environment}-values.yaml"
enable=$(yq eval '.customHost.enabled' "$config_file")

if [ "$enable" = "true" ]; then
  url=$(yq eval '.customHost.url' "$config_file")
else
  url="$DEFAULT_URL"
fi

echo "URL: $url"

response=$(curl -s https://dev-app.matrixenergia.com/auto-dns/check_dns/$url )

if [[ "$response" == *"\"exist\": true"* ]]; then
    echo "DNS already exists"
else
    second_response=$(curl --location --request POST https://dev-app.matrixenergia.com/auto-dns/create_dns/$url )
    echo "creating a new dns register with: $url,     $second_response"
fi