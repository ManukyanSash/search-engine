import sys
sys.path.append("QueryProcessor")
from QueryProcessor.server import Engine

if __name__ == "__main__":
    engine = Engine()
    engine.start()