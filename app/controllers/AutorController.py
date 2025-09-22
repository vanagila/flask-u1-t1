from flask import Blueprint, render_template

autor_bp = Blueprint('autor', __name__)

@autor_bp.route('/autor')
def autor():
    return render_template('autor/autor.html')
