import sys
sys.dont_write_bytecode = True

from src.main import app


if __name__ == '__main__':
    host = '0.0.0.0'
    port=5000
    app.run(debug=True, host=host, port=port)
    