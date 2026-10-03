"""A small demo website that we run our tests against.
It has a login page, a task list (add / delete) and a simple JSON API."""
from flask import Flask, jsonify, redirect, render_template, request, session, url_for

USERS = {"admin": "admin123", "tester": "test@123"}


def create_app():
    app = Flask(__name__)
    app.secret_key = "demo-secret"
    seeded_tasks = [
        "Check login with wrong password",
        "Test add and delete task",
    ]
    state = {
        "items": [{"id": index + 1, "name": name} for index, name in enumerate(seeded_tasks)],
        "next_id": len(seeded_tasks) + 1,
    }

    def add_item(name):
        item = {"id": state["next_id"], "name": name}
        state["items"].append(item)
        state["next_id"] += 1
        return item

    @app.route("/")
    def index():
        return redirect(url_for("dashboard" if "user" in session else "login"))

    @app.route("/login", methods=["GET", "POST"])
    def login():
        error = None
        if request.method == "POST":
            u, p = request.form.get("username", ""), request.form.get("password", "")
            if not u or not p:
                error = "Username and password are required"
            elif USERS.get(u) == p:
                session["user"] = u
                return redirect(url_for("dashboard"))
            else:
                error = "Invalid credentials"
        return render_template("login.html", error=error)

    @app.route("/dashboard")
    def dashboard():
        if "user" not in session:
            return redirect(url_for("login"))
        return render_template("dashboard.html", user=session["user"], items=state["items"],
                               msg=request.args.get("msg"))

    @app.route("/add", methods=["POST"])
    def add():
        if "user" not in session:
            return redirect(url_for("login"))
        name = request.form.get("item", "").strip()
        if not name:
            return redirect(url_for("dashboard", msg="Item cannot be empty"))
        add_item(name)
        return redirect(url_for("dashboard"))

    @app.route("/delete/<int:item_id>", methods=["POST"])
    def delete(item_id):
        state["items"][:] = [i for i in state["items"] if i["id"] != item_id]
        return redirect(url_for("dashboard"))

    @app.route("/logout")
    def logout():
        session.clear()
        return redirect(url_for("login"))

    # API part (used by tests/api)
    @app.route("/api/health")
    def health():
        return jsonify(status="ok")

    @app.route("/api/items", methods=["GET", "POST"])
    def api_items():
        if request.method == "POST":
            data = request.get_json(silent=True) or {}
            name = str(data.get("name", "")).strip()
            if not name:
                return jsonify(error="name is required"), 400
            return jsonify(add_item(name)), 201
        return jsonify(state["items"])

    @app.route("/api/items/<int:item_id>", methods=["DELETE"])
    def api_delete(item_id):
        before = len(state["items"])
        state["items"][:] = [i for i in state["items"] if i["id"] != item_id]
        if len(state["items"]) == before:
            return jsonify(error="not found"), 404
        return "", 204

    return app


if __name__ == "__main__":
    create_app().run(port=5055, debug=False)
