import json
import os

# Clase para manejar el almacenamiento del conocimiento
class KnowledgeModule:
    def __init__(self, knowledge_file='knowledge.json'):
        self.knowledge_file = knowledge_file
        # Cargar conocimiento previo si el archivo existe, de lo contrario iniciar con un diccionario vacío
        if os.path.exists(self.knowledge_file):
            with open(self.knowledge_file, 'r') as f:
                self.knowledge = json.load(f)
        else:
            self.knowledge = {}

    # Guardar el conocimiento en un archivo JSON
    def save_knowledge(self):
        with open(self.knowledge_file, 'w') as f:
            json.dump(self.knowledge, f, indent=4)

    # Recuperar una respuesta basada en una pregunta si existe
    def get_response(self, question):
        return self.knowledge.get(question.lower())

    # Almacenar una nueva pregunta y su respuesta
    def store_response(self, question, response):
        self.knowledge[question.lower()] = response
        self.save_knowledge()


# Clase del Chatbot
class Chatbot:
    def __init__(self):
        self.knowledge_module = KnowledgeModule()

    # Función principal para interactuar con el usuario
    def chat(self):
        print("¡Hola! Soy tu chatbot. Pregúntame algo.")
        
        while True:
            user_input = input("Tú: ").strip().lower()

            if user_input == "salir":
                print("Chatbot: ¡Adiós! Hasta luego.")
                break

            # Recuperar la respuesta si la pregunta ya ha sido almacenada
            stored_response = self.knowledge_module.get_response(user_input)

            if stored_response:
                print(f"Chatbot: {stored_response}")
            else:
                # Si no hay una respuesta almacenada, preguntar al usuario qué respuesta debería almacenar
                response = input(f"Chatbot: No sé la respuesta a '{user_input}'. ¿Cuál debería ser la respuesta? ")
                self.knowledge_module.store_response(user_input, response)
                print(f"Chatbot: ¡Gracias! Recordaré que la respuesta a '{user_input}' es '{response}'.")

# Ejecutar el chatbot
if __name__ == "__main__":
    chatbot = Chatbot()
    chatbot.chat()
