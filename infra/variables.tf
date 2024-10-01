variable "function_name" {
  type        = string
  default     = "postech-token-generator"
}

variable "function_role" {
  type        = string
  default     = "arn:aws:iam::975748149223:role/LabRole"
}

variable "handler" {
  type        = string
  default     = "main.lambda_handler"
}

variable "runtime" {
  type        = string
  default     = "python3.8"
}

variable "timeout" {
  type        = number
  default     = 60
}