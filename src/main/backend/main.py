from fastapi import FastAPI, Query
from kubernetes import client, config
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def load_cluster(context="minikube"):
    config.load_kube_config(context=context)

@app.get("/")
def home():
    return {"message": "RBAC Manager Running"}

@app.get("/roles")
def get_roles(context: str = Query("minikube")):
    load_cluster(context)
    api = client.RbacAuthorizationV1Api()
    roles = api.list_role_for_all_namespaces()
    
    result = []
    for r in roles.items:
    	result.append({
        	"name": r.metadata.name,
        	"namespace": r.metadata.namespace,
        	"rules": [rule.to_dict() for rule in r.rules] if r.rules else [],
        	"status": "Safe"
    	})
    return result
   
@app.post("/create-role")
def create_role(name: str, namespace: str):
    api = client.RbacAuthorizationV1Api()

    role = client.V1Role(
        metadata=client.V1ObjectMeta(
            name=name,
            namespace=namespace
        ),
        rules=[
            client.V1PolicyRule(
                api_groups=[""],
                resources=["pods"],
                verbs=["get", "list"]
            )
        ]
    )

    api.create_namespaced_role(namespace, role)
    return {"message": f"Role {name} created in {namespace}"}

@app.delete("/delete-role")
def delete_role(name: str, namespace: str):
    api = client.RbacAuthorizationV1Api()
    api.delete_namespaced_role(name, namespace)
    return {"message": f"Role {name} deleted"}

@app.get("/bindings")
def get_bindings():
    api = client.RbacAuthorizationV1Api()
    bindings = api.list_role_binding_for_all_namespaces()
    
    result = []
    for b in bindings.items:
        subjects = []

        if b.subjects is not None:
            for s in b.subjects:
                subjects.append(f"{s.kind}:{s.name}")

        result.append({
            "name": b.metadata.name,
            "namespace": b.metadata.namespace,
            "subjects": subjects if subjects else ["None"]
        })

    return result
