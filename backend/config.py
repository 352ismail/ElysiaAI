import os 
def main():
    if "GOOGLE_API_KEY" not in os.environ:
        os.environ["GOOGLE_API_KEY"] = "AIzaSyAqx_F8RNkh5vFABJYKsBFh_A4FPOcZ0vE"
        
    if "BACKEND_URL" not in os.environ:
        os.environ["BACKEND_URL"] = "http://localhost:8000/ask"
    
if __name__ == "__main__":
    main()