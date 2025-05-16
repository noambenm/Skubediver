# calculator-service/main.py
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/calc/po2")
def calc_po2():
    # Example: /calc/po2?fraction_o2=0.32&depth=30
    try:
        fo2 = float(request.args.get('fraction_o2'))
        depth = float(request.args.get('depth'))
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid parameters"}), 400
    # PO2 (in bar) = FO2 * (ambient pressure), ambient pressure = depth/10 + 1
    po2 = fo2 * ((depth / 10) + 1)
    return jsonify({"po2": round(po2, 2)})

@app.route("/calc/mod")
def calc_mod():
    # Example: /calc/mod?fraction_o2=0.32&po2=1.4
    try:
        fo2 = float(request.args.get('fraction_o2'))
        target_po2 = float(request.args.get('po2'))
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid parameters"}), 400
    # MOD (in m) = 10 * ((PO2 / FO2) - 1)
    if fo2 == 0:
        return jsonify({"error": "FO2 cannot be 0"}), 400
    mod = 10 * ((target_po2 / fo2) - 1)
    return jsonify({"mod_meters": round(mod, 1)})

if __name__ == "__main__":
    port = int(os.getenv('PORT', 5003))
    app.run(host="0.0.0.0", port=port)
