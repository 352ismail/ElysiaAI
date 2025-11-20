def parse_ai_response(response_data: dict) -> str:
    try:
        if not response_data or not isinstance(response_data, dict):
            return ""

        model_section = response_data.get("model", {})
        messages = model_section.get("messages", [])

        if not messages:
            return ""
        last_message = messages[-1]

        if hasattr(last_message, "content") and last_message.content:
            return last_message.content.strip()
        elif isinstance(last_message, dict) and "content" in last_message:
            return last_message["content"].strip()
        else:
            return ""

    except Exception as e:
        return f"I am sorry, I have some technical difficulties right now. Please try again later."
    
    

