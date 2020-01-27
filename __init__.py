import logging
from flask import Flask, render_template

# -------------Logger structure------------
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M:%S')
logger = logging.getLogger('Portfolio')
# ------------------------------------------

app = Flask(__name__)


@app.route('/')
def rendering_template():
    try:
        return render_template('interactive_terminal.html')
    except Exception as e:
        return(str(e))


if __name__ == '__main__':
    app.run()
