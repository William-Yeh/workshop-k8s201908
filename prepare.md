## 行前準備

為了活動進行順利，請在出席活動前，確實備妥下列事項。


### 關於你的筆電

- 請先在你的筆電上，熟悉任何一種終端機軟體的基本操作。尤其是 Windows 用戶，不妨試試更好用的 Cmder，甚至 [Windows Terminal (preview)](https://www.microsoft.com/zh-tw/p/windows-terminal-preview/9n0dx20hk701)。

- 請先在自備筆電中安裝 [Docker Desktop](https://www.docker.com/products/docker-desktop)，並開啟其中的 Kubernetes 功能。

- 請先在自備筆電中安裝 [Skaffold](https://skaffold.dev/)。

- 請先下載 ASP.NET Core 相關 images，以節省現場操作時間：

  ```
  docker pull mcr.microsoft.com/dotnet/core/sdk:2.2
  docker pull mcr.microsoft.com/dotnet/core/aspnet:2.2
  ```



### 關於 Google Cloud


- 為了活動進行順利，請在出席活動前，依照【[GKE 相關工作坊行前須知](http://bit.ly/gke-workshops-note)】所述的三大步驟確實完成。我會預期所有出席活動的人，都學會 [Google Cloud Shell](https://cloud.google.com/shell/) 基本操作，也都早已經設定好正確的 Project ID 了。

- 本次活動現場有提供實作所需的 GCP 額度。



### 其他事項

- 請先熟悉 git 基本操作，尤其是 `clone` 及 `checkout`。
