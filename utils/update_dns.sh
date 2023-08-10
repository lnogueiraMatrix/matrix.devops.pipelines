environment=$(echo "$ENVIRONMENT" | tr '[:upper:]' '[:lower:]')

config_file=".ci/${environment}-values.yaml"
config=$(yaml2json < "$config_file")

custom_host=$(echo "$config" | jq -r '.customHost')
enable=$(echo "$custom_host" | jq -r '.enabled')

if [ "$enable" = "true" ]; then
  url=$(echo "$custom_host" | jq -r '.url')
else
  url="$DEFAULT_URL"
fi

echo "URL: $url"

response=$(curl -s https://dev-app.matrixenergia.com/auto-dns/check_dns/$url )

if [[ "$response" == *"\"exist\": true"* ]]; then
    echo "A primeira API retornou 'exist': true"
else
    echo "A primeira API retornou 'exist': false"
    
    # Chamar a segunda API
    second_response=$(curl --location --request POST https://dev-app.matrixenergia.com/auto-dns/create_dns/$url )
    echo "Resposta da segunda API: $second_response"
fi