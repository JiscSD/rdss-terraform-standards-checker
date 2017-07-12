output "arn" {
  value = "${aws_kinesis_stream.kinesis_stream.arn}"
}

output "name" {
  value = "${aws_kinesis_stream.kinesis_stream.name}"
}
