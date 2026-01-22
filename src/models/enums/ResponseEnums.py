from enum import Enum

class ResponseSignal(Enum):
    FILE_TYPE_NOT_SUPPORTED = "file_type_not_supported"
    FILE_SIZE_EXCEEDED = "file_size_exceeded."
    FILE_VALIDATED_SUCCESSFULLY = "file_validated_successfully"

    
# Enums members are ready-to-use object
    