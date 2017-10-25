from settings import *
from views import *
from models import *


if __name__ == '__main__':
    model_init()
    app.run(debug=True, host='0.0.0.0', port=80)
