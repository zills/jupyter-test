try_catch() {
  local retries=$1
  local delay=$2
  local command=$3
  local quiet=$4

  for i in $(seq 1 $retries); do
    if [ "$quiet" = "quite" ]; then
            output=$($command) > /dev/null && return 0
    else
            output=$($command) && return 0
    fi
    echo "Command failed, retrying in $delay seconds..."
    sleep $delay
  done

  echo "Command failed after $retries retries: $command"
  return 1
}
