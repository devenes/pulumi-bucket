# Infrastructure as Code with Pulumi

## 1. Install Pulumi

- Follow the instructions at [Pulumi Doc.](https://www.pulumi.com/docs/get-started/install/) to install Pulumi.

- If you are using a Mac, you can install Pulumi with Homebrew:

  ```bash
  brew install pulumi
  ```

- If you are using Windows, you can install Pulumi with Chocolatey:

  ```bash
  choco install pulumi
  ```

- If you are using Linux, you can install Pulumi with Snap:

  ```bash
  snap install pulumi --classic
  ```

## 2. Install Language Runtime for virtual environment

```bash
install python3-venv python3-pip
```

## 3. Configure Pulumi to access your AWS account

- If you are using Windows, you can use the following command to configure Pulumi to access your AWS account:

```bash
pulumi config set aws:region us-east-1
pulumi config set aws:accessKey <YOUR_ACCESS_KEY_ID>
pulumi config set aws:secretKey <YOUR_SECRET_ACCESS_KEY>
```

or

```bash
$env:AWS_ACCESS_KEY_ID = "<YOUR_ACCESS_KEY_ID>"
$env:AWS_SECRET_ACCESS_KEY = "<YOUR_SECRET_ACCESS_KEY>"
```

or if you are using Linux or Mac:

```bash
export AWS_ACCESS_KEY_ID="<YOUR_ACCESS_KEY_ID>"
export AWS_SECRET_ACCESS_KEY="<YOUR_SECRET_ACCESS_KEY>"
```

## 4. Create a New Project

```bash
pulumi new aws-pulumi-s3
```

## 5. Deploy stack

```bash
pulumi up
```

## 6. Get the output of the stack

```bash
pulumi stack output bucket_name
```

## 7. Updated with index.html and run

```bash
pulumi up
```

## 8. Verify the object was created in your bucket

```bash
aws s3 ls $(pulumi stack output bucket_name)
```

## 9. Deploy the Stack

```bash
pulumi destroy
```
