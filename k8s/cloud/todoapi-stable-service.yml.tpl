---
apiVersion: v1
kind: Service
metadata:
  name: todoapi
  labels:
    app: todo
    tier: backend
spec:
  type: LoadBalancer
  loadBalancerIP: TODOAPI_IP_ADDR  # external IP (ephemeral or static)
  ports:
    - name: http
      port: 80
      targetPort: 80
  selector:
    app: todo
    tier: backend

---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: todoapi
  labels:
    app: todo
    tier: backend
    track: stable

spec:
  replicas: 3
  selector:
    matchLabels:
      app: todo
      tier: backend
  strategy:
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 1
    type: RollingUpdate

  template:   # pod definition
    metadata:
      labels:
        app: todo
        tier: backend
    spec:
      containers:
        # STABLE track -- use "stable" tag here!
        - name: todoapi
          image: gcr.io/PROJECT_ID/todoapi:stable
          imagePullPolicy: IfNotPresent
          ports:
            - containerPort: 80
      #dnsPolicy: ClusterFirst
      #restartPolicy: Always
