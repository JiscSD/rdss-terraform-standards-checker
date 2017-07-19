variable "stream_name" {
  description = "A name to identify the stream. Must be unique to AWS account and region the Stream is created in."
}

variable "shard_count" {
  description = "Number of shards the stream will use."
  default     = 1
}

variable "retention_period" {
  description = "Number of hours data records are accessible for after they are added to the stream."
  default     = 168
}
