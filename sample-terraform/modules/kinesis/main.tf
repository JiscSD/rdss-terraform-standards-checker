##############################
# Manage AWS Kinesis Streams #
##############################

resource "aws_kinesis_stream" "kinesis_0stream" {
  name             = "${var.stream_name}"
  shard_count      = "${var.shard_count}"
  retention_period = "${var.retention_period}"
}
