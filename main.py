from settings import *
from views import *
from ajax import *
import command
from models import *
import orm

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8111)
