---json
{
  "id": "documentacao-kubernetes",
  "title": "Kubernetes — Guia Completo (Descomplicando K8s)",
  "categoria": "06-devops-infra",
  "subcategoria": "linux",
  "resumo": "**Nota:** Na prática, use **Deployments** que gerenciam ReplicaSets automaticamente. Pods serão nomeados: `mysql-0`, `mysql-1`, `mysql-2` (identidade estável).",
  "gatilhos": [
    "completo",
    "descomplicando",
    "devops",
    "documentacao",
    "guia",
    "infra",
    "k8s",
    "kubernetes"
  ],
  "perguntas_tipo": [
    "Como utilizar Kubernetes — Guia Completo (Descomplicando K8s)?",
    "Quais as boas praticas de linux?"
  ],
  "nao_cobre": [],
  "target_agent": [
    "general-assistant"
  ],
  "source": {
    "origin": "AllMight Knowledge Base",
    "original_format": "markdown"
  },
  "atualizado_em": "2026-10-15",
  "verificado_em": "2026-10-15",
  "dono": "stack-linux",
  "prioridade": 2
}
---

# Kubernetes — Guia Completo (Descomplicando K8s)

**Fontes:**
- [livro.descomplicandokubernetes.com.br](https://livro.descomplicandokubernetes.com.br/pt/) — LINUXtips (Days 1-16)
- [kubernetes.io/docs](https://kubernetes.io/docs/home/)

**Versão:** Kubernetes 1.29+  
**Categoria:** DevOps · Orquestração de Containers  
**Última Atualização do Conteúdo:** 2026-02-14  
**Último Acesso às Fontes:** 2026-02-14

---

## Sumário (Trilha Day 1–16)

| Day | Tema | Nível |
|---|---|---|
| [1](#day-1) | O que é Kubernetes? Arquitetura, kubectl, Kind | Básico |
| [2](#day-2) | Pods — criação, YAML, volumes EmptyDir, limites | Básico |
| [3](#day-3) | Deployments — estratégias, rollout, rollback | Básico |
| [4](#day-4) | ReplicaSet, DaemonSet, Probes | Intermediário |
| [5](#day-5) | Instalação de cluster (kubeadm) | Expert |
| [6](#day-6) | Volumes, PV, PVC, StorageClass | Intermediário |
| [7](#day-7) | StatefulSet, Services, Headless | Intermediário |
| [8](#day-8) | Secrets, ConfigMaps | Intermediário |
| [9](#day-9) | Ingress, Nginx Ingress Controller, EKS | Avançado |
| [10](#day-10) | Cert-Manager, Labels, Annotations, Canary | Avançado |
| [11](#day-11) | Metrics Server, HPA | Avançado |
| [12](#day-12) | Taints, Tolerations, Affinity | Avançado |
| [13](#day-13) | Kyverno — Policies de Segurança | Avançado |
| [14](#day-14) | Network Policies | Avançado |
| [15](#day-15) | RBAC, ServiceAccounts, Tokens | Avançado |
| [16](#day-16) | Helm Charts | Avançado |

---

<a id="day-1"></a>
## DAY 1 — O que é Kubernetes?

### Origem
O Kubernetes (K8s) foi desenvolvido pelo Google em 2014, baseado nos sistemas internos **Borg** e **Omega** que gerenciavam containers em larga escala. O nome vem do grego "timoneiro". A abreviação K8s segue o padrão i18n (k + 8 letras + s).

### Arquitetura

```
┌──────────────────────────────────────────────────────┐
│                   CONTROL PLANE                       │
│  ┌──────────┐ ┌──────────┐ ┌────────┐ ┌──────────┐  │
│  │ API      │ │ etcd     │ │ Sched  │ │ Ctrl Mgr │  │
│  │ Server   │ │ (banco)  │ │ uler   │ │          │  │
│  └──────────┘ └──────────┘ └────────┘ └──────────┘  │
└──────────────────────────────────────────────────────┘
                        │
       ┌────────────────┼────────────────┐
       ▼                ▼                ▼
┌──────────────┐ ┌──────────────┐ ┌──────────────┐
│   NODE 1     │ │   NODE 2     │ │   NODE 3     │
│  kubelet     │ │  kubelet     │ │  kubelet     │
│  kube-proxy  │ │  kube-proxy  │ │  kube-proxy  │
│  container   │ │  container   │ │  container   │
│  runtime     │ │  runtime     │ │  runtime     │
└──────────────┘ └──────────────┘ └──────────────┘
```

| Componente | Função |
|---|---|
| **API Server** | Ponto de entrada para todas as operações (REST) |
| **etcd** | Banco key-value distribuído que armazena todo o estado |
| **Scheduler** | Decide em qual Node um Pod será executado |
| **Controller Manager** | Garante que o estado desejado = estado atual |
| **kubelet** | Agente em cada Node, gerencia ciclo de vida dos Pods |
| **kube-proxy** | Rede, iptables, regras de Service |

### Portas importantes

| Componente | Porta | Protocolo |
|---|---|---|
| API Server | 6443 | TCP |
| etcd | 2379-2380 | TCP |
| kubelet | 10250 | TCP |
| kube-scheduler | 10259 | TCP |
| kube-controller | 10257 | TCP |
| NodePort range | 30000-32767 | TCP |

### Instalação (Kind — Kubernetes IN Docker)

```bash
# Instalar Kind
curl -Lo ./kind https://kind.sigs.k8s.io/dl/latest/kind-linux-amd64
chmod +x ./kind && sudo mv ./kind /usr/local/bin/kind

# Criar cluster simples
kind create cluster --name meu-cluster

# Cluster multi-node
cat << EOF > kind-config.yaml
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
nodes:
  - role: control-plane
  - role: worker
  - role: worker
  - role: worker
EOF
kind create cluster --name multi-node --config kind-config.yaml

# Instalar kubectl
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
chmod +x kubectl && sudo mv kubectl /usr/local/bin/

# Verificar
kubectl cluster-info
kubectl get nodes
```

### Customizando kubectl

```bash
# Alias
alias k=kubectl
echo 'alias k=kubectl' >> ~/.bashrc

# Autocompletion
source <(kubectl completion bash)
echo 'source <(kubectl completion bash)' >> ~/.bashrc

# Habilitar completion para alias
complete -o default -F __start_kubectl k
```

---

<a id="day-2"></a>
## DAY 2 — Pods

O **Pod** é a menor unidade no Kubernetes. Contém um ou mais containers que compartilham rede (IP), namespace e volumes.

### Criando Pods via CLI

```bash
# Criar Pod
kubectl run giropops --image=nginx --port=80

# Criar Pod dry-run (gerar YAML)
kubectl run giropops --image=nginx --port=80 --dry-run=client -o yaml > pod.yaml

# Listar Pods
kubectl get pods                           # Namespace default
kubectl get pods -A                        # Todas namespaces
kubectl get pods -o wide                   # Com IP e Node
kubectl get pods -o yaml                   # YAML completo
kubectl get pods -o json                   # JSON completo

# Detalhes
kubectl describe pod giropops

# Logs
kubectl logs giropops
kubectl logs giropops -f                   # Follow

# Shell no Pod
kubectl exec -it giropops -- /bin/bash
kubectl attach giropops -c container-name

# Deletar
kubectl delete pod giropops
```

### Pod via YAML

```yaml
# pod.yaml
apiVersion: v1
kind: Pod
metadata:
  name: giropops
  labels:
    app: giropops
    env: production
spec:
  containers:
    - name: giropops
      image: nginx:1.25
      ports:
        - containerPort: 80
      resources:
        requests:
          memory: "64Mi"
          cpu: "250m"
        limits:
          memory: "128Mi"
          cpu: "500m"
```

```bash
kubectl apply -f pod.yaml
```

### Pod com Volume EmptyDir

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: pod-com-volume
spec:
  containers:
    - name: app
      image: nginx
      volumeMounts:
        - mountPath: /dados
          name: dados-volume
    - name: sidecar
      image: busybox
      command: ["sh", "-c", "while true; do date >> /dados/log.txt; sleep 5; done"]
      volumeMounts:
        - mountPath: /dados
          name: dados-volume
  volumes:
    - name: dados-volume
      emptyDir: {}
```

---

<a id="day-3"></a>
## DAY 3 — Deployments

O **Deployment** gerencia ReplicaSets e garante o número desejado de réplicas. Permite rolling updates e rollbacks.

```yaml
# deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  labels:
    app: nginx
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxUnavailable: 1
      maxSurge: 1
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
        - name: nginx
          image: nginx:1.25
          ports:
            - containerPort: 80
          resources:
            requests:
              memory: "128Mi"
              cpu: "250m"
            limits:
              memory: "256Mi"
              cpu: "500m"
```

### Operações com Deployments

```bash
kubectl apply -f deployment.yaml
kubectl get deployments
kubectl get replicasets

# Escalar
kubectl scale deployment nginx-deployment --replicas=5

# Atualizar imagem (rolling update)
kubectl set image deployment/nginx-deployment nginx=nginx:1.26

# Status do rollout
kubectl rollout status deployment/nginx-deployment

# Histórico de revisões
kubectl rollout history deployment/nginx-deployment
kubectl rollout history deployment/nginx-deployment --revision=2

# Rollback
kubectl rollout undo deployment/nginx-deployment
kubectl rollout undo deployment/nginx-deployment --to-revision=1

# Pausar/resumir rollout
kubectl rollout pause deployment/nginx-deployment
kubectl rollout resume deployment/nginx-deployment
```

### Estratégias de Deploy

| Estratégia | Comportamento |
|---|---|
| **RollingUpdate** | Atualiza gradualmente (padrão) |
| **Recreate** | Mata todos os Pods antes de criar os novos |

---

<a id="day-4"></a>
## DAY 4 — ReplicaSet, DaemonSet e Probes

### ReplicaSet

Garante que um número específico de réplicas está sempre rodando.

```yaml
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: nginx-replicaset
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
        - name: nginx
          image: nginx:1.25
          resources:
            limits: { cpu: "500m", memory: "256Mi" }
            requests: { cpu: "250m", memory: "128Mi" }
```

> **Nota:** Na prática, use **Deployments** que gerenciam ReplicaSets automaticamente.

### DaemonSet

Garante que **um Pod rode em cada Node** do cluster. Ideal para: logs, monitoring, network plugins.

```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: node-exporter
spec:
  selector:
    matchLabels:
      app: node-exporter
  template:
    metadata:
      labels:
        app: node-exporter
    spec:
      containers:
        - name: node-exporter
          image: prom/node-exporter:latest
          ports:
            - containerPort: 9100
          resources:
            limits: { cpu: "200m", memory: "128Mi" }
            requests: { cpu: "100m", memory: "64Mi" }
      hostNetwork: true
```

### Probes (Health Checks)

| Probe | Finalidade | Se falhar |
|---|---|---|
| **livenessProbe** | App está viva? | Reinicia o container |
| **readinessProbe** | App pronta para receber tráfego? | Remove do Service |
| **startupProbe** | App já inicializou? | Aguarda (bloqueia as demais) |

```yaml
spec:
  containers:
    - name: app
      image: meu-app:1.0
      livenessProbe:
        httpGet:
          path: /health
          port: 80
        initialDelaySeconds: 10
        periodSeconds: 10
        timeoutSeconds: 5
        failureThreshold: 3
      readinessProbe:
        httpGet:
          path: /ready
          port: 80
        initialDelaySeconds: 5
        periodSeconds: 3
      startupProbe:
        httpGet:
          path: /started
          port: 80
        failureThreshold: 30
        periodSeconds: 10
```

#### Tipos de verificação

```yaml
# HTTP GET
livenessProbe:
  httpGet:
    path: /health
    port: 8080

# TCP Socket
livenessProbe:
  tcpSocket:
    port: 3306

# Exec Command
livenessProbe:
  exec:
    command: ["cat", "/tmp/healthy"]
```

---

<a id="day-5"></a>
## DAY 5 — Instalação de Cluster (kubeadm)

### Pré-requisitos (cada node)
```bash
# Desabilitar swap
sudo swapoff -a

# Instalar containerd
sudo apt-get update && sudo apt-get install -y containerd

# Configurar containerd
sudo mkdir -p /etc/containerd
containerd config default | sudo tee /etc/containerd/config.toml
sudo systemctl restart containerd

# Instalar kubeadm, kubelet, kubectl
sudo apt-get install -y apt-transport-https ca-certificates curl
curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.29/deb/Release.key | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg
echo 'deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.29/deb/ /' | sudo tee /etc/apt/sources.list.d/kubernetes.list
sudo apt-get update && sudo apt-get install -y kubelet kubeadm kubectl
sudo apt-mark hold kubelet kubeadm kubectl
```

### Inicializar Control Plane
```bash
sudo kubeadm init --pod-network-cidr=10.10.0.0/16 --apiserver-advertise-address=<IP>

# Configurar kubectl
mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config

# Instalar CNI (Weave Net)
kubectl apply -f https://github.com/weaveworks/weave/releases/download/v2.8.1/weave-daemonset-k8s.yaml
```

### Adicionar Workers
```bash
# No control plane, gerar token
kubeadm token create --print-join-command

# Em cada worker, executar o comando gerado
sudo kubeadm join <IP>:6443 --token <token> --discovery-token-ca-cert-hash sha256:<hash>
```

---

<a id="day-6"></a>
## DAY 6 — Volumes, PV, PVC, StorageClass

### Tipos de Volume

| Tipo | Persistência | Uso |
|---|---|---|
| **emptyDir** | Vida do Pod | Cache, dados temporários |
| **hostPath** | Vida do Node | Dev, acesso a arquivos do host |
| **PersistentVolume** | Independente | Produção |
| **NFS** | Rede | Compartilhamento entre Pods |

### PersistentVolume (PV) e PersistentVolumeClaim (PVC)

```yaml
# PV — definido pelo admin
apiVersion: v1
kind: PersistentVolume
metadata:
  name: meu-pv
spec:
  capacity:
    storage: 10Gi
  accessModes:
    - ReadWriteOnce
  persistentVolumeReclaimPolicy: Retain
  hostPath:
    path: /mnt/data

---
# PVC — solicitado pelo desenvolvedor
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: meu-pvc
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 5Gi

---
# Usando no Pod
apiVersion: v1
kind: Pod
metadata:
  name: app-com-storage
spec:
  containers:
    - name: app
      image: nginx
      volumeMounts:
        - mountPath: /dados
          name: storage
  volumes:
    - name: storage
      persistentVolumeClaim:
        claimName: meu-pvc
```

### StorageClass (provisionamento dinâmico)

```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: fast-storage
provisioner: kubernetes.io/aws-ebs
parameters:
  type: gp3
  fsType: ext4
reclaimPolicy: Delete
allowVolumeExpansion: true
```

---

<a id="day-7"></a>
## DAY 7 — StatefulSet e Services

### StatefulSet

Para apps que precisam de **identidade estável** e **storage persistente por Pod** (bancos de dados, Kafka, etc).

```yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: mysql
spec:
  serviceName: "mysql"
  replicas: 3
  selector:
    matchLabels:
      app: mysql
  template:
    metadata:
      labels:
        app: mysql
    spec:
      containers:
        - name: mysql
          image: mysql:8.0
          env:
            - name: MYSQL_ROOT_PASSWORD
              value: "root123"
          ports:
            - containerPort: 3306
          volumeMounts:
            - name: data
              mountPath: /var/lib/mysql
  volumeClaimTemplates:
    - metadata:
        name: data
      spec:
        accessModes: ["ReadWriteOnce"]
        resources:
          requests:
            storage: 10Gi
```

> Pods serão nomeados: `mysql-0`, `mysql-1`, `mysql-2` (identidade estável).

### Types de Service

```yaml
# ClusterIP (padrão — interno)
apiVersion: v1
kind: Service
metadata:
  name: app-service
spec:
  selector:
    app: web
  ports:
    - port: 80
      targetPort: 3000
  type: ClusterIP

---
# NodePort (acesso externo via porta do node)
apiVersion: v1
kind: Service
metadata:
  name: app-nodeport
spec:
  selector:
    app: web
  ports:
    - port: 80
      targetPort: 3000
      nodePort: 30080
  type: NodePort

---
# LoadBalancer (cloud)
apiVersion: v1
kind: Service
metadata:
  name: app-lb
spec:
  selector:
    app: web
  ports:
    - port: 80
      targetPort: 3000
  type: LoadBalancer

---
# Headless (StatefulSet — retorna IPs dos Pods)
apiVersion: v1
kind: Service
metadata:
  name: mysql
spec:
  selector:
    app: mysql
  ports:
    - port: 3306
  clusterIP: None   # <-- Headless
```

---

<a id="day-8"></a>
## DAY 8 — Secrets e ConfigMaps

### ConfigMap

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  APP_ENV: "production"
  APP_PORT: "3000"
  LOG_LEVEL: "info"
  nginx.conf: |
    server {
      listen 80;
      location / { proxy_pass http://app:3000; }
    }
```

### Secret

```bash
# Criar via CLI
kubectl create secret generic db-secret \
  --from-literal=username=admin \
  --from-literal=password=senha123

# Criar via YAML
echo -n "admin" | base64      # YWRtaW4=
echo -n "senha123" | base64   # c2VuaGExMjM=
```

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: db-secret
type: Opaque
data:
  username: YWRtaW4=
  password: c2VuaGExMjM=
```

### Usando no Deployment

```yaml
spec:
  containers:
    - name: app
      env:
        # De Secret
        - name: DB_USER
          valueFrom:
            secretKeyRef:
              name: db-secret
              key: username
        # De ConfigMap
        - name: APP_PORT
          valueFrom:
            configMapKeyRef:
              name: app-config
              key: APP_PORT
      # Ou montar como volume
      volumeMounts:
        - name: config-volume
          mountPath: /etc/nginx/nginx.conf
          subPath: nginx.conf
  volumes:
    - name: config-volume
      configMap:
        name: app-config
```

---

<a id="day-9"></a>
## DAY 9 — Ingress

O **Ingress** gerencia acesso externo HTTP/HTTPS, permitindo roteamento por host/path, TLS, e load balancing.

### Instalar Nginx Ingress Controller

```bash
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.9.4/deploy/static/provider/cloud/deploy.yaml
```

### Recurso Ingress

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: app-ingress
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  ingressClassName: nginx
  rules:
    - host: meuapp.com
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: frontend-service
                port:
                  number: 80
          - path: /api
            pathType: Prefix
            backend:
              service:
                name: backend-service
                port:
                  number: 3000
  tls:
    - hosts:
        - meuapp.com
      secretName: tls-secret
```

### Múltiplos Ingresses

```yaml
# Ingress para app1.com
- host: app1.com
  http:
    paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: app1-service
            port:
              number: 80
# Ingress para app2.com
- host: app2.com
  http:
    paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: app2-service
            port:
              number: 80
```

---

<a id="day-10"></a>
## DAY 10 — Cert-Manager, Labels, Annotations, Canary

### Cert-Manager (HTTPS automático)

```bash
# Instalar
kubectl apply -f https://github.com/cert-manager/cert-manager/releases/download/v1.14.0/cert-manager.yaml

# ClusterIssuer para Let's Encrypt
```

```yaml
apiVersion: cert-manager.io/v1
kind: ClusterIssuer
metadata:
  name: letsencrypt-prod
spec:
  acme:
    server: https://acme-v02.api.letsencrypt.org/directory
    email: admin@meuapp.com
    privateKeySecretRef:
      name: letsencrypt-prod
    solvers:
      - http01:
          ingress:
            class: nginx
```

### Labels e Annotations

```bash
# Labels — usados para seleção e filtragem
kubectl label pod meu-pod app=web env=production
kubectl get pods -l app=web
kubectl get pods -l 'env in (production, staging)'

# Annotations — metadados informativos
kubectl annotate pod meu-pod description="Pod principal"
```

### Canary Deployment com Ingress

```yaml
# Ingress canary (10% do tráfego para versão nova)
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: app-canary
  annotations:
    nginx.ingress.kubernetes.io/canary: "true"
    nginx.ingress.kubernetes.io/canary-weight: "10"
spec:
  ingressClassName: nginx
  rules:
    - host: meuapp.com
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: app-v2-service
                port:
                  number: 80
```

---

<a id="day-11"></a>
## DAY 11 — Metrics Server e HPA

### Instalar Metrics Server

```bash
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml

# Verificar
kubectl top nodes
kubectl top pods
```

### HPA (Horizontal Pod Autoscaler)

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: app-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: web-app
  minReplicas: 2
  maxReplicas: 10
  metrics:
    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          averageUtilization: 50
    - type: Resource
      resource:
        name: memory
        target:
          type: Utilization
          averageUtilization: 70
```

```bash
kubectl get hpa
kubectl describe hpa app-hpa

# Teste de carga (para ver HPA em ação)
kubectl run -i --tty load-generator --rm --image=busybox --restart=Never -- /bin/sh -c "while sleep 0.01; do wget -q -O- http://web-app; done"
```

---

<a id="day-12"></a>
## DAY 12 — Taints, Tolerations e Affinity

### Taints (no Node)

"Manchas" nos Nodes que repelem Pods sem Tolerations correspondentes.

```bash
# Aplicar Taint
kubectl taint nodes worker1 key=value:NoSchedule
kubectl taint nodes worker1 gpu=true:NoExecute
kubectl taint nodes worker1 environment=production:PreferNoSchedule

# Remover Taint
kubectl taint nodes worker1 key=value:NoSchedule-

# Ver Taints
kubectl describe node worker1 | grep Taints
```

| Efeito | Comportamento |
|---|---|
| **NoSchedule** | Não agenda novos Pods |
| **PreferNoSchedule** | Tenta evitar, mas não garante |
| **NoExecute** | Remove Pods existentes sem Toleration |

### Tolerations (no Pod)

```yaml
spec:
  tolerations:
    - key: "gpu"
      operator: "Equal"
      value: "true"
      effect: "NoSchedule"
    - key: "environment"
      operator: "Equal"
      value: "production"
      effect: "NoExecute"
      tolerationSeconds: 3600
```

### Node Affinity

```yaml
spec:
  affinity:
    nodeAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        nodeSelectorTerms:
          - matchExpressions:
              - key: disktype
                operator: In
                values: ["ssd"]
      preferredDuringSchedulingIgnoredDuringExecution:
        - weight: 1
          preference:
            matchExpressions:
              - key: zone
                operator: In
                values: ["us-east-1a"]
```

### Pod Anti-Affinity (distribuir Pods entre Nodes)

```yaml
spec:
  affinity:
    podAntiAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        - labelSelector:
            matchExpressions:
              - key: app
                operator: In
                values: ["web"]
          topologyKey: "kubernetes.io/hostname"
```

---

<a id="day-13"></a>
## DAY 13 — Kyverno (Policies de Segurança)

### O que é Kyverno?
Ferramenta de **validação**, **mutação** e **geração** de recursos Kubernetes via policies declarativas.

### Instalar

```bash
helm repo add kyverno https://kyverno.github.io/kyverno/
helm repo update
helm install kyverno kyverno/kyverno --namespace kyverno --create-namespace

# Verificar
kubectl get pods -n kyverno
kubectl get crd | grep kyverno
```

### Exemplos de Policies

```yaml
# Exigir limites de recursos
apiVersion: kyverno.io/v1
kind: ClusterPolicy
metadata:
  name: require-resource-limits
spec:
  validationFailureAction: Enforce
  rules:
    - name: require-limits
      match:
        any:
          - resources:
              kinds: ["Pod"]
      validate:
        message: "CPU e memória limits são obrigatórios."
        pattern:
          spec:
            containers:
              - resources:
                  limits:
                    memory: "?*"
                    cpu: "?*"

---
# Adicionar label automaticamente (mutação)
apiVersion: kyverno.io/v1
kind: ClusterPolicy
metadata:
  name: add-team-label
spec:
  rules:
    - name: add-label
      match:
        any:
          - resources:
              kinds: ["Pod"]
      mutate:
        patchStrategicMerge:
          metadata:
            labels:
              team: "platform"
```

---

<a id="day-14"></a>
## DAY 14 — Network Policies

Controlam o tráfego de rede entre Pods (semelhante a firewall rules).

```yaml
# Bloquear todo tráfego (deny all)
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: deny-all
  namespace: production
spec:
  podSelector: {}
  policyTypes:
    - Ingress
    - Egress

---
# Permitir tráfego apenas do frontend para backend
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-frontend-to-backend
spec:
  podSelector:
    matchLabels:
      app: backend
  policyTypes:
    - Ingress
  ingress:
    - from:
        - podSelector:
            matchLabels:
              app: frontend
      ports:
        - protocol: TCP
          port: 3000

---
# Permitir DNS (egress)
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-dns
spec:
  podSelector: {}
  policyTypes:
    - Egress
  egress:
    - to: []
      ports:
        - protocol: UDP
          port: 53
        - protocol: TCP
          port: 53
```

---

<a id="day-15"></a>
## DAY 15 — RBAC (Role-Based Access Control)

### Conceitos

| Recurso | Escopo | Função |
|---|---|---|
| **Role** | Namespace | Permissões dentro de um namespace |
| **ClusterRole** | Cluster | Permissões em todo o cluster |
| **RoleBinding** | Namespace | Liga Role a User/Group/ServiceAccount |
| **ClusterRoleBinding** | Cluster | Liga ClusterRole a User/Group/ServiceAccount |

### Criar usuário com certificado

```bash
# 1. Gerar chave privada
openssl genrsa -out developer.key 2048

# 2. Criar CSR (Certificate Signing Request)
openssl req -new -key developer.key -out developer.csr -subj "/CN=developer"

# 3. Enviar CSR ao Kubernetes
cat developer.csr | base64 | tr -d '\n'
```

```yaml
# CSR no Kubernetes
apiVersion: certificates.k8s.io/v1
kind: CertificateSigningRequest
metadata:
  name: developer
spec:
  request: <BASE64_DO_CSR>
  signerName: kubernetes.io/kube-apiserver-client
  usages: ["client auth"]
```

```bash
# 4. Aprovar
kubectl certificate approve developer

# 5. Extrair certificado
kubectl get csr developer -o jsonpath='{.status.certificate}' | base64 -d > developer.crt
```

### Role + RoleBinding

```yaml
# Role — permissões para Pods no namespace dev
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  namespace: dev
  name: pod-manager
rules:
  - apiGroups: [""]
    resources: ["pods", "pods/log"]
    verbs: ["get", "list", "watch", "create", "delete"]
  - apiGroups: ["apps"]
    resources: ["deployments"]
    verbs: ["get", "list"]

---
# RoleBinding — associa Role ao usuário
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: developer-pod-manager
  namespace: dev
subjects:
  - kind: User
    name: developer
    apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: Role
  name: pod-manager
  apiGroup: rbac.authorization.k8s.io
```

### ServiceAccount + Token

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: monitoring-sa
  namespace: monitoring

---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: monitoring-reader
subjects:
  - kind: ServiceAccount
    name: monitoring-sa
    namespace: monitoring
roleRef:
  kind: ClusterRole
  name: view
  apiGroup: rbac.authorization.k8s.io
```

```bash
# Criar token para ServiceAccount
kubectl create token monitoring-sa -n monitoring --duration=8760h
```

---

<a id="day-16"></a>
## DAY 16 — Helm (Gerenciador de Pacotes)

### Instalar Helm

```bash
curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
chmod 700 get_helm.sh && ./get_helm.sh

# Verificar
helm version
```

### Criar Chart

```bash
helm create meu-app  # Gera estrutura padrão
```

```
meu-app/
├── Chart.yaml           # Metadados do chart
├── values.yaml          # Valores padrão (configuráveis)
├── templates/
│   ├── deployment.yaml  # Template do Deployment
│   ├── service.yaml     # Template do Service
│   ├── ingress.yaml     # Template do Ingress
│   ├── hpa.yaml         # Template do HPA
│   ├── _helpers.tpl     # Funções helper
│   └── NOTES.txt        # Mensagem pós-install
└── charts/              # Dependências
```

### Templates com valores

```yaml
# templates/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ .Release.Name }}-{{ .Chart.Name }}
  labels:
    app: {{ .Values.app.name }}
spec:
  replicas: {{ .Values.replicaCount }}
  selector:
    matchLabels:
      app: {{ .Values.app.name }}
  template:
    spec:
      containers:
        - name: {{ .Values.app.name }}
          image: "{{ .Values.image.repository }}:{{ .Values.image.tag }}"
          ports:
            - containerPort: {{ .Values.service.targetPort }}
          resources:
            {{- toYaml .Values.resources | nindent 12 }}
```

```yaml
# values.yaml
replicaCount: 3

app:
  name: meu-app

image:
  repository: nginx
  tag: "1.25"

service:
  type: ClusterIP
  port: 80
  targetPort: 80

resources:
  requests:
    cpu: "250m"
    memory: "128Mi"
  limits:
    cpu: "500m"
    memory: "256Mi"
```

### Comandos Helm

```bash
# Instalar
helm install meu-release ./meu-app
helm install meu-release ./meu-app -f producao-values.yaml
helm install meu-release ./meu-app --set replicaCount=5

# Listar releases
helm list
helm list -A

# Atualizar
helm upgrade meu-release ./meu-app --set image.tag=2.0

# Rollback
helm rollback meu-release 1

# Desinstalar
helm uninstall meu-release

# Template (dry-run — ver YAML gerado)
helm template meu-release ./meu-app

# Instalar chart de repositório
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update
helm install my-wordpress bitnami/wordpress
```

---

## BÔNUS — Tópicos Oficiais kubernetes.io

> Os tópicos a seguir são da **documentação oficial** (`kubernetes.io/docs`) e complementam o livro "Descomplicando K8s".

---

### Jobs (tarefas pontuais)

Um **Job** cria Pods que executam até conclusão (batch processing). Diferente de Deployments, que mantêm Pods eternamente.

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: migrate-db
spec:
  completions: 1          # Quantas execuções com sucesso
  parallelism: 1          # Pods paralelos
  backoffLimit: 4          # Retentativas em caso de falha
  activeDeadlineSeconds: 600  # Timeout total
  ttlSecondsAfterFinished: 100  # Auto-limpar após 100s
  template:
    spec:
      containers:
        - name: migration
          image: meu-app:migrate
          command: ["python", "manage.py", "migrate"]
      restartPolicy: Never  # Obrigatório para Jobs
```

```bash
kubectl get jobs
kubectl describe job migrate-db
kubectl logs job/migrate-db
```

---

### CronJobs (tarefas agendadas)

```yaml
apiVersion: batch/v1
kind: CronJob
metadata:
  name: backup-diario
spec:
  schedule: "30 2 * * *"         # Todo dia às 02:30
  concurrencyPolicy: Forbid       # Não executar se anterior ainda roda
  successfulJobsHistoryLimit: 3   # Manter 3 últimos jobs bem-sucedidos
  failedJobsHistoryLimit: 1       # Manter 1 job falhado
  startingDeadlineSeconds: 200    # Deadline para iniciar
  suspend: false                   # Pausar cron
  jobTemplate:
    spec:
      template:
        spec:
          containers:
            - name: backup
              image: meu-app:backup
              command: ["/bin/sh", "-c", "pg_dump mydb > /backup/dump.sql"]
          restartPolicy: OnFailure
```

#### Sintaxe Cron

```
┌───────────── minuto (0-59)
│ ┌─────────── hora (0-23)
│ │ ┌───────── dia do mês (1-31)
│ │ │ ┌─────── mês (1-12)
│ │ │ │ ┌───── dia da semana (0-6 = Dom-Sáb)
│ │ │ │ │
* * * * *
```

| Expressão | Significado |
|---|---|
| `*/5 * * * *` | A cada 5 minutos |
| `0 * * * *` | A cada hora |
| `0 0 * * *` | Meia-noite diariamente |
| `0 2 * * 0` | Domingos às 02:00 |
| `0 0 1 * *` | Primeiro dia de cada mês |

---

### ResourceQuota (controle de recursos por namespace)

Limita consumo agregado de recursos por namespace — essencial em clusters multi-tenant.

```yaml
apiVersion: v1
kind: ResourceQuota
metadata:
  name: team-quota
  namespace: team-a
spec:
  hard:
    # Computação
    requests.cpu: "10"
    requests.memory: "20Gi"
    limits.cpu: "20"
    limits.memory: "40Gi"
    # Objetos
    pods: "50"
    services: "10"
    secrets: "20"
    configmaps: "20"
    persistentvolumeclaims: "10"
    # Storage
    requests.storage: "100Gi"
```

```bash
kubectl get resourcequota -n team-a
kubectl describe resourcequota team-quota -n team-a
```

---

### LimitRange (limites padrão por container)

Define **min/max/default** para containers que não especificam recursos.

```yaml
apiVersion: v1
kind: LimitRange
metadata:
  name: default-limits
  namespace: production
spec:
  limits:
    - type: Container
      default:           # Valor padrão se não definido
        cpu: "500m"
        memory: "256Mi"
      defaultRequest:    # Request padrão se não definido
        cpu: "250m"
        memory: "128Mi"
      min:               # Mínimo permitido
        cpu: "100m"
        memory: "64Mi"
      max:               # Máximo permitido
        cpu: "2"
        memory: "2Gi"
    - type: Pod
      max:
        cpu: "4"
        memory: "4Gi"
```

---

### PriorityClass (prioridade de Pods)

Pods de alta prioridade podem **preemptar** (expulsar) Pods de baixa prioridade quando não há recursos.

```yaml
# Definir classes de prioridade
apiVersion: scheduling.k8s.io/v1
kind: PriorityClass
metadata:
  name: critical-apps
value: 1000000
globalDefault: false
preemptionPolicy: PreemptLowerPriority
description: "Apps críticas de produção"

---
apiVersion: scheduling.k8s.io/v1
kind: PriorityClass
metadata:
  name: batch-jobs
value: 100
preemptionPolicy: Never  # Não expulsa outros
description: "Jobs batch de baixa prioridade"
```

```yaml
# Usar no Pod/Deployment
spec:
  priorityClassName: critical-apps
  containers:
    - name: app
      image: meu-app:prod
```

---

### Pod Security Standards (segurança nativa)

3 níveis de segurança definidos pelo Kubernetes (substituem PodSecurityPolicy):

| Perfil | Restrições | Uso |
|---|---|---|
| **Privileged** | Nenhuma restrição | System/infra (Istio, CNI) |
| **Baseline** | Bloqueia escalações conhecidas | Maioria das apps |
| **Restricted** | Boas práticas rigorosas | Apps sensíveis |

```bash
# Aplicar via labels no namespace
kubectl label namespace production \
  pod-security.kubernetes.io/enforce=baseline \
  pod-security.kubernetes.io/warn=restricted \
  pod-security.kubernetes.io/audit=restricted
```

| Modo | Comportamento |
|---|---|
| **enforce** | Rejeita Pods que violam |
| **warn** | Permite, mas exibe aviso no kubectl |
| **audit** | Registra no audit log |

---

### Logging Architecture

```bash
# Logs básicos
kubectl logs <pod>
kubectl logs <pod> -c <container>  # Multi-container
kubectl logs <pod> --previous      # Container anterior (crash)
kubectl logs <pod> -f              # Follow (tempo real)
kubectl logs <pod> --tail=100      # Últimas 100 linhas
kubectl logs <pod> --since=1h      # Última hora

# Logs de todos os Pods de um Deployment
kubectl logs deployment/web-app --all-containers=true
kubectl logs -l app=web --all-containers=true
```

#### Arquiteturas de Logging em Cluster

| Abordagem | Como funciona | Ferramentas |
|---|---|---|
| **Node agent** | DaemonSet coleta logs de cada node | Fluentd, Fluent Bit, Filebeat |
| **Sidecar** | Container auxiliar no Pod captura logs | Fluentd sidecar |
| **Direto** | App envia logs direto ao backend | App → Elasticsearch |

```yaml
# Exemplo: Fluent Bit como DaemonSet
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: fluent-bit
  namespace: logging
spec:
  selector:
    matchLabels:
      app: fluent-bit
  template:
    metadata:
      labels:
        app: fluent-bit
    spec:
      serviceAccountName: fluent-bit
      containers:
        - name: fluent-bit
          image: fluent/fluent-bit:latest
          volumeMounts:
            - name: varlog
              mountPath: /var/log
            - name: containers
              mountPath: /var/lib/docker/containers
              readOnly: true
      volumes:
        - name: varlog
          hostPath:
            path: /var/log
        - name: containers
          hostPath:
            path: /var/lib/docker/containers
```

---

### Namespaces (isolamento de recursos)

Mecanismo para isolar grupos de recursos dentro de um cluster. Essencial em ambientes multi-tenant.

#### Namespaces Iniciais

| Namespace | Função |
|---|---|
| `default` | Recursos sem namespace explícito |
| `kube-system` | Componentes do sistema (etcd, kube-dns, etc.) |
| `kube-public` | Recursos públicos, legíveis por todos |
| `kube-node-lease` | Heartbeats dos Nodes (Lease objects) |

```bash
# Criar e gerenciar
kubectl create namespace staging
kubectl get namespaces
kubectl delete namespace staging

# Definir namespace padrão no contexto
kubectl config set-context --current --namespace=production

# Listar recursos em namespace específico
kubectl get pods -n kube-system
kubectl get all -n production

# Listar recursos NÃO namespaced (cluster-wide)
kubectl api-resources --namespaced=false
```

#### DNS inter-namespace

```
# Dentro do MESMO namespace:
meu-service

# ENTRE namespaces:
meu-service.outro-namespace.svc.cluster.local
```

---

### Init Containers (inicialização antes da app)

Containers especiais que **rodam antes** dos containers da aplicação. Cada init container deve completar com sucesso antes do próximo iniciar.

**Casos de uso:**
- Esperar que um banco de dados ou serviço esteja pronto
- Fazer download de configurações/assets
- Rodar migrações de schema
- Configurar permissões em volumes compartilhados

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: app-com-init
spec:
  initContainers:
    - name: wait-for-db
      image: busybox:1.28
      command: ['sh', '-c', 'until nslookup postgres-service; do echo "Aguardando DB..."; sleep 2; done']
    - name: download-config
      image: busybox:1.28
      command: ['wget', '-O', '/config/app.conf', 'http://config-server/app.conf']
      volumeMounts:
        - name: config-vol
          mountPath: /config
  containers:
    - name: app
      image: meu-app:latest
      volumeMounts:
        - name: config-vol
          mountPath: /app/config
  volumes:
    - name: config-vol
      emptyDir: {}
```

---

### Sidecar Containers (v1.33 stable)

Containers secundários que rodam **junto** com o container principal durante toda a vida do Pod. Definidos como init containers com `restartPolicy: Always`.

**Casos de uso:** Logging, proxies (Envoy/Istio), sync de dados, monitoramento.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: app-com-sidecar
spec:
  initContainers:
    - name: log-shipper            # Sidecar
      image: fluent/fluent-bit
      restartPolicy: Always        # <-- Torna sidecar
      volumeMounts:
        - name: logs
          mountPath: /var/log/app
  containers:
    - name: app
      image: meu-app:latest
      volumeMounts:
        - name: logs
          mountPath: /var/log/app
  volumes:
    - name: logs
      emptyDir: {}
```

| Tipo | Inicia | Termina | `restartPolicy` |
|---|---|---|---|
| **Init Container** | Antes da app | Antes da app iniciar | Never/OnFailure |
| **Sidecar** | Antes da app | Quando Pod termina | Always |
| **App Container** | Após inits | Quando Pod termina | Herdado do Pod |

---

### Ephemeral Containers (debug em produção)

Containers temporários injetados em Pods **já em execução** para diagnóstico. Não requerem rebuild da imagem.

```bash
# Injetar container de debug num Pod em execução
kubectl debug -it meu-pod --image=busybox --target=app-container

# Debug com imagem rica em ferramentas
kubectl debug -it meu-pod --image=nicolaka/netshoot --target=app-container

# Criar cópia do Pod com debug container
kubectl debug meu-pod -it --image=ubuntu --share-processes --copy-to=debug-pod

# Debug de Node (cria Pod privilegiado no Node)
kubectl debug node/worker-1 -it --image=ubuntu
```

> **Nota:** Ephemeral containers não suportam ports, resources (limits/requests), probes, nem `restartPolicy`. São exclusivos para troubleshooting.

---

### PodDisruptionBudget — PDB (alta disponibilidade)

Garante um número **mínimo de Pods saudáveis** durante eventos de disrupção voluntária (drain, upgrade de Node, rolling update).

```yaml
apiVersion: policy/v1
kind: PodDisruptionBudget
metadata:
  name: web-pdb
spec:
  minAvailable: 2         # Pelo menos 2 Pods sempre rodando
  selector:
    matchLabels:
      app: web

---
# Alternativa: maxUnavailable
apiVersion: policy/v1
kind: PodDisruptionBudget
metadata:
  name: api-pdb
spec:
  maxUnavailable: 1        # No máximo 1 Pod fora por vez
  selector:
    matchLabels:
      app: api

---
# Com porcentagem
apiVersion: policy/v1
kind: PodDisruptionBudget
metadata:
  name: workers-pdb
spec:
  maxUnavailable: "25%"    # No máximo 25% fora por vez
  selector:
    matchLabels:
      app: worker
```

```bash
kubectl get pdb
kubectl describe pdb web-pdb
```

> ⚠️ **Cuidado:** `maxUnavailable: 0` impede `kubectl drain` completamente.

---

### Gateway API (evolução do Ingress)

A **Gateway API** é o sucessor do Ingress, oferecendo roteamento mais expressivo, role-oriented, e suporte nativo a HTTP/gRPC.

| Recurso | Função |
|---|---|
| **GatewayClass** | Define o controlador (ex: Nginx, Envoy, Istio) |
| **Gateway** | Instância de infra de tráfego (load balancer) |
| **HTTPRoute** | Regras HTTP (hosts, paths, headers, weights) |
| **GRPCRoute** | Regras gRPC |

```yaml
# GatewayClass (admin do cluster)
apiVersion: gateway.networking.k8s.io/v1
kind: GatewayClass
metadata:
  name: envoy-gateway
spec:
  controllerName: gateway.envoyproxy.io/gatewayclass-controller

---
# Gateway (operador de infra)
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  name: meu-gateway
spec:
  gatewayClassName: envoy-gateway
  listeners:
    - name: http
      protocol: HTTP
      port: 80
    - name: https
      protocol: HTTPS
      port: 443
      tls:
        mode: Terminate
        certificateRefs:
          - name: meu-cert

---
# HTTPRoute (desenvolvedor)
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: app-route
spec:
  parentRefs:
    - name: meu-gateway
  hostnames:
    - "app.example.com"
  rules:
    - matches:
        - path:
            type: PathPrefix
            value: /api
      backendRefs:
        - name: api-service
          port: 8080
          weight: 90
        - name: api-v2-service
          port: 8080
          weight: 10         # Canary 10%
    - matches:
        - path:
            type: PathPrefix
            value: /
      backendRefs:
        - name: frontend-service
          port: 80
```

#### Ingress vs Gateway API

| Aspecto | Ingress | Gateway API |
|---|---|---|
| **Maturidade** | Stable (legacy) | Stable (v1.0+) |
| **Role separation** | Tudo no mesmo YAML | GatewayClass / Gateway / Route |
| **Protocolos** | HTTP/HTTPS | HTTP, gRPC, TCP, TLS |
| **Traffic splitting** | Via annotation | Nativo (weight) |
| **Header matching** | Via annotation | Nativo |
| **Extensibilidade** | Annotations do provider | CRDs padronizados |

---

## Cheatsheet Completo

```bash
# ===== CLUSTER =====
kubectl cluster-info
kubectl get nodes
kubectl top nodes
kubectl get namespaces
kubectl create namespace meu-ns

# ===== PODS =====
kubectl get pods [-A] [-o wide] [-l app=web]
kubectl describe pod <nome>
kubectl logs <pod> [-f] [-c container]
kubectl exec -it <pod> -- /bin/bash
kubectl port-forward <pod> 8080:80
kubectl delete pod <pod>

# ===== DEPLOYMENTS =====
kubectl get deployments
kubectl scale deployment <nome> --replicas=5
kubectl set image deployment/<nome> <container>=<img:tag>
kubectl rollout status/undo/history deployment/<nome>

# ===== SERVICES =====
kubectl get services
kubectl expose deployment <nome> --port=80 --type=LoadBalancer

# ===== CONFIGMAPS & SECRETS =====
kubectl create configmap <nome> --from-literal=key=value
kubectl create secret generic <nome> --from-literal=key=value

# ===== TAINTS =====
kubectl taint nodes <node> key=value:NoSchedule
kubectl taint nodes <node> key=value:NoSchedule-

# ===== RBAC =====
kubectl create serviceaccount <nome>
kubectl create token <sa-nome>
kubectl auth can-i get pods --as=developer -n dev

# ===== HELM =====
helm install/upgrade/rollback/uninstall <release> <chart>
helm list [-A]
helm template <release> <chart>

# ===== GERAL =====
kubectl apply -f <arquivo.yaml>
kubectl delete -f <arquivo.yaml>
kubectl get all [-n namespace]
kubectl api-resources
kubectl explain <resource>
```

---

## Docker vs Kubernetes

| Aspecto | Docker (Compose) | Kubernetes |
|---|---|---|
| **Escopo** | Cria/executa containers | Orquestra em escala |
| **Scale** | Manual | Automático (HPA) |
| **Self-healing** | Reinicia container | Recria Pod em outro Node |
| **Networking** | Bridge/overlay | Service discovery nativo |
| **Load Balance** | Nginx manual | Service + Ingress |
| **Storage** | Volumes locais | PV/PVC (cloud-native) |
| **Segurança** | Limitada | RBAC, NetworkPolicy, Kyverno |
| **Deploy** | `docker compose up` | Rolling update, Canary, Blue/Green |
| **Quando usar** | Dev local, projetos pequenos | Produção, microserviços |

---

*Fontes: [Descomplicando Kubernetes — LINUXtips](https://livro.descomplicandokubernetes.com.br/pt/) (Days 1-16) · [kubernetes.io/docs](https://kubernetes.io/docs/home/) — Acessado em 2026-02-14*
