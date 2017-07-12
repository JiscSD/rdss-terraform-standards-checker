


resource "aws_iam" "test" {
  name = "Test"
}

resource "something" "invalid-name" {
  name = "test"
}

module "some-module" {
  // Test
  source            = "./modules/kinesis"
  stream_name       = "institution_${var.jisc_id}_input_${terraform.env}"
  shard_count       = "${var.kinesis_shard_count}"
  retention_period  = "${var.kinesis_retention_period}"
}
