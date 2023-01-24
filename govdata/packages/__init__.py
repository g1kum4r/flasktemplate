from flask import Blueprint
bp = Blueprint('packages', __name__)
import govdata.packages.routes