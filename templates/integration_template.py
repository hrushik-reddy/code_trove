import logging
from typing import Dict, List, Optional, Literal, Annotated
from pydantic import Field, BaseModel
from integrations.IntegrationBase import IntegrationBase, IntegrationSetupBase
from utils.utils import accumulator, get_setup_details, decrypt_string
from utils.utils_traceability import AITrace, TraceBase
from utils.agent_enums import DisplayFormat


class {IntegrationName}SetupConfig(IntegrationSetupBase):
    """
    Configuration class for the integration setup.
    Define all the parameters needed for initialization.
    """
    # Required parameters
    api_key: str = Field(..., 
                         description="API key for {IntegrationName}", 
                         encryptionRequired=True)
    
    # Optional parameters with default values
    action: Optional[Literal["action1", "action2", "action3"]] = Field("action1", 
                                                                     description="The task to be performed")
    max_results: Optional[int] = Field(3, 
                                      description="Maximum number of results to return", 
                                      ge=1, le=10)
    # Add more parameters as needed


class {IntegrationName}Trace(TraceBase):
    """
    Trace class for tracking and debugging integration execution.
    """
    # Input trace
    user_query: str = Field(..., 
                           description="Input query for the integration", 
                           title="Input Query", 
                           displayOnCard=True)
    
    # Config parameters for tracing
    action: str = Field(..., 
                       description="Action performed", 
                       title="Action")
    max_results: int = Field(..., 
                            description="Maximum results configured", 
                            title="Max Results")
    
    # Output trace
    result: dict = Field(..., 
                        description="Results from the integration", 
                        title="Output Response", 
                        displayOnCard=True)


class {IntegrationName}Integration(IntegrationBase):
    def setup(self, concierge_id=None, integration_id=None, config: Optional[dict] = None,
              header_messages: Optional[dict] = {}):
        """
        Initialize the integration with the provided configuration.
        
        Args:
            concierge_id: ID of the concierge (required if config is not provided)
            integration_id: ID of the integration (required if config is not provided)
            config: Configuration dictionary
            header_messages: Optional messages to display during operation
        """
        if config is None:
            assert integration_id is not None, "If config is not provided integration_id is a required parameter"
            assert concierge_id is not None, "If config is not provided concierge_id is a required parameter"

            # Fetch config details from database
            config = get_setup_details(concierge_id, integration_id)

        super().setup(config=config)
        
        # Initialize required parameters
        self.api_key = decrypt_string(config["api_key"])
        
        # Initialize optional parameters with defaults
        self.action = config.get("action", {IntegrationName}SetupConfig.get_default_value('action'))
        self.max_results = config.get("max_results", {IntegrationName}SetupConfig.get_default_value('max_results'))
        
        # Initialize client
        self.client = self._initialize_client()
        
        # Additional setup steps
        logging.info(f"{IntegrationName} client setup complete")

    def _initialize_client(self):
        """
        Initialize and return the API client
        """
        try:
            # Import the appropriate client library if needed
            # Example: from third_party_lib import ClientClass
            # return ClientClass(api_key=self.api_key)
            
            # Or return a custom client configuration
            return {
                "api_key": self.api_key,
                "initialized": True
            }
        except Exception as e:
            self.error = f"Error initializing {IntegrationName} client: {str(e)}"
            logging.error(self.error)
            raise Exception(self.error)

    @AITrace({IntegrationName}Trace)
    def run(self, query: Annotated[str, "The input query for the integration."], 
            next_trace=None, trace=None) -> Dict:
        """
        Execute the integration with the provided query.
        
        Args:
            query (str): The input query
            next_trace: Trace information for the next operation
            trace: Current trace information
            
        Returns:
            dict: Results from the integration
        """
        try:
            self.user_query = query
            
            if self.action == "action1":
                self.result = self._perform_action1(query)
            elif self.action == "action2":
                self.result = self._perform_action2(query)
            elif self.action == "action3":
                self.result = self._perform_action3(query)
            else:
                raise ValueError(f"Invalid action: {self.action}. Supported actions are 'action1', 'action2', and 'action3'.")
                
            return self.result
            
        except Exception as e:
            self.error = f"Error in {IntegrationName} integration: {str(e)}"
            logging.error(self.error)
            raise Exception(self.error)
    
    def _perform_action1(self, query: str) -> Dict:
        """
        Implementation for action1
        """
        try:
            # Implementation code here
            # Example: response = self.client.search(query=query, max_results=self.max_results)
            response = {"result": "Action1 executed with query: " + query}
            return response
        except Exception as e:
            self.error = f"{IntegrationName} API error in action1: {str(e)}"
            logging.error(self.error)
            raise Exception(self.error)
    
    def _perform_action2(self, query: str) -> Dict:
        """
        Implementation for action2
        """
        try:
            # Implementation code here
            response = {"result": "Action2 executed with query: " + query}
            return response
        except Exception as e:
            self.error = f"{IntegrationName} API error in action2: {str(e)}"
            logging.error(self.error)
            raise Exception(self.error)
    
    def _perform_action3(self, query: str) -> Dict:
        """
        Implementation for action3
        """
        try:
            # Implementation code here
            response = {"result": "Action3 executed with query: " + query}
            return response
        except Exception as e:
            self.error = f"{IntegrationName} API error in action3: {str(e)}"
            logging.error(self.error)
            raise Exception(self.error)

    @classmethod
    def get_setup_config(cls) -> dict:
        """
        Return the setup configuration schema
        """
        return accumulator({IntegrationName}SetupConfig, cls.__name__)