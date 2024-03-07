from flask import Flask, request, jsonify

from langchain_community.llms import Bedrock  
from langchain_core.prompts import PromptTemplate

app = Flask(__name__)

@app.route("/translate", methods=["POST"])  
def translate():
    try:
        data = request.get_json()
        text = data["text"]
        style = data["style"]

        prompt = PromptTemplate(
            template="Translate this into a {style} style: {text}",
            input_variables=["text", "style"]
        )
        
        llm = Bedrock(model_id="anthropic.claude-v2", model_kwargs={"temperature": 0}) 

        output = llm(prompt.format(text=text, style=style))
        # print(type(output))
        # output = str(output)
        return jsonify({"translated_text": output})
    except Exception as e:
        print(e)
        return {"error": str(e)}, 500


if __name__ == "__main__":
    app.run(port=5000)