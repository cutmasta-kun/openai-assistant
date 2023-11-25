from pydantic import BaseModel, Field
from typing import Optional, Dict, List, Union

class FunctionToolParameters(BaseModel):
    type: str = Field(..., description="The type of the parameters object, typically 'object'.")
    properties: Dict[str, Union[Dict, None]] = Field({}, description="The properties of the parameters, described as a JSON Schema object.")

class FunctionTool(BaseModel):
    type: str = Field(..., description="The type of tool, which is function.")
    description: str = Field(..., description="A description of what the function does.")
    name: str = Field(..., max_length=64, regex="^[a-zA-Z0-9_-]+$", description="The name of the function to be called.")
    parameters: FunctionToolParameters = Field(..., description="The parameters the function accepts.")

class Assistant(BaseModel):
    id: Optional[str] = Field(None, description="The identifier, which can be referenced in API endpoints.")
    name: Optional[str] = Field(None, max_length=256, description="The name of the assistant.")
    description: Optional[str] = Field(None, max_length=512, description="The description of the assistant.")
    model: str = Field(..., description="ID of the model to use.")
    instructions: Optional[str] = Field(None, max_length=32768, description="The system instructions for the assistant.")
    tools: List[FunctionTool] = Field(..., description="A list of function tools enabled on the assistant.")
    file_ids: List[str] = Field(..., description="A list of file IDs attached to this assistant.")
    metadata: Dict[str, str] = Field(..., description="Set of key-value pairs attached to the object.")
