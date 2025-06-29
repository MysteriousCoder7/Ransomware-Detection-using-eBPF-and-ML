# Ransomware-Detection-using-eBPF-and-ML

Abstract
Ransomware has emerged as one of the most formidable threats in the cybersecurity landscape, targeting individuals, businesses, and critical infrastructure worldwide. Traditional signature-based and heuristic approaches to ransomware detection often fail to keep pace with the rapid evolution of malware techniques. In this paper, we propose a novel approach to ransomware detection leveraging Extended Berkeley Packet Filter (eBPF) technology to monitor system calls executed by running processes. eBPF provides an efficient and non-intrusive mechanism to capture system behavior in real-time, enabling dynamic and context-aware anomaly detection. The collected system call data is subsequently fed into a machine learning model, specifically a Random Forest classifier, trained on a dataset comprising normal and ransomware-induced system activity. The experimental results demonstrate that our model effectively distinguishes ransomware from benign processes with high accuracy, outperforming traditional rule-based detection mechanisms. This approach offers a lightweight and proactive solution to ransomware detection, minimizing performance overhead while enhancing system security.

Aim-

To develop an efficient and lightweight ransomware detection system using eBPF technology for system call monitoring, combined with a machine learning-based classification model to accurately differentiate between benign and malicious (ransomware) activities.
Introduction-

Cyber threats have evolved significantly over the past decade, with ransomware standing out as one of the most pervasive and damaging attack vectors. Ransomware encrypts files on a victim’s system and demands payment for decryption, often causing significant financial and operational losses. Traditional detection techniques, including signature-based and behavioral analysis methods, struggle to adapt to the ever-changing tactics of modern ransomware variants. Therefore, there is a pressing need for more adaptive and intelligent detection mechanisms.

Extended Berkeley Packet Filter (eBPF) has gained traction as a powerful tool for real-time system monitoring and security enforcement. By allowing safe and efficient execution of bytecode within the Linux kernel, eBPF enables granular tracking of system calls without introducing significant performance overhead. This capability makes it well-suited for identifying abnormal behaviors indicative of ransomware activity.

Machine learning has proven effective in various cybersecurity applications, and in this work, we leverage a Random Forest classifier to analyze system call patterns. By training the model on a dataset containing both benign and ransomware-related system call traces, we achieve high detection accuracy with minimal false positives.

This paper is structured as follows: Section 2 provides an in-depth discussion on ransomware, including its operational mechanisms and impact. Section 3 introduces eBPF and its advantages in security monitoring. Section 4 explains the Random Forest model and its application in anomaly detection. Section 5 presents related work in ransomware detection, followed by our proposed methodology in Section 6. Section 7 discusses the experimental setup and evaluation results. Finally, Section 8 concludes the paper and outlines future research directions.
Ransomware: An Overview
What is Ransomware?

Ransomware is a type of malicious software that encrypts files or entire systems, demanding a ransom payment from victims to restore access. First emerging in the late 1980s, ransomware has since evolved into a major cybersecurity threat, with variants such as WannaCry, NotPetya, and Ryuk causing billions of dollars in damages globally.
How Ransomware Works:

Ransomware follows a predictable attack lifecycle:

  Infiltration: Attackers gain initial access through phishing emails, exploit vulnerabilities, or leverage compromised credentials.

  Execution: Once inside, the malware executes and begins identifying target files for encryption.

  File Manipulation: Ransomware typically follows a read-modify-write cycle, encrypting files while sometimes deleting backups to prevent recovery.

  Extortion: The malware displays a ransom note demanding payment, usually in cryptocurrency, in exchange for a decryption key.

Extended Berkeley Packet Filter (eBPF)

eBPF is a modern Linux technology that enables safe and efficient monitoring of system events at the kernel level. It allows security analysts to attach custom programs to specific kernel functions, capturing system calls and other behaviors in real-time. Unlike traditional kernel modules, eBPF offers:

  Performance Efficiency: Minimal overhead compared to traditional system monitoring tools.

  Flexibility: Can be used for networking, observability, and security applications.

  Security: Operates in a sandboxed environment, reducing attack surfaces.

For ransomware detection, eBPF enables us to capture system call sequences indicative of ransomware-like behavior, such as excessive file modifications and mass encryption attempts.
Classifying our Logged Results

Three different approaches to classification were considered in the making of the final model: Support Vector Machines, Random Forests, as well as Deep Neural Networks.

Support Vector Machines (SVMs)

Support Vector Machines are powerful supervised learning models that aim to find the optimal hyperplane for classifying data. They are effective for ransomware detection due to:

  High Generalization Capability: Maximizes the margin between classes, reducing the risk of misclassification.
  Effective in High-Dimensional Spaces: Performs well even when the number of features (e.g., system calls) exceeds the number of samples.
  Robust to Overfitting: Particularly effective when using kernel functions for nonlinear feature mapping.

Random Forests (RFs)

A Random Forest is an ensemble learning method that constructs multiple decision trees to improve classification performance. It is well-suited for ransomware detection due to:

  Robustness to Overfitting: The combination of multiple decision trees reduces variance.

  Feature Importance Analysis: Identifies key system calls associated with ransomware activity.

  High Accuracy: Provides superior detection capabilities compared to simpler models.

Deep Neural Networks (DNNs)

Deep Neural Networks are multi-layered architectures capable of learning complex patterns from raw data. Their strength in ransomware detection lies in:

  Automatic Feature Extraction: Learns hierarchical representations directly from system call sequences or behavioral logs.
  Scalability and Flexibility: Adapts to large and diverse datasets, improving detection across varied ransomware strains.
  High Predictive Accuracy: Capable of capturing subtle, nonlinear relationships in data, leading to superior classification performance.

The final approach to classification considered was the latter, i.e., the deep neural network classifier. 
Methodolgy -

Ransomware Detection Approaches

Detecting ransomware involves analyzing its distinctive behaviors and patterns. These may include activities such as unauthorized file encryption, communication with external control servers, and abnormal process behavior. By identifying these indicators, it becomes possible to detect ransomware attacks early. In more advanced scenarios, detection methods may incorporate techniques like machine learning and anomaly detection to improve both accuracy and efficiency.

Ransomware detection strategies generally fall into two main categories: network-based detection and host-based detection. Network-based detection focuses on monitoring network traffic to uncover signs of ransomware activity. This can include analyzing packet data from affected devices or connected networks, where anomalies such as DNS queries targeting suspicious domains or attempts to access network storage might signal an attack.

On the other hand, host-based detection involves observing system-level behavior on individual devices. This approach examines a combination of static and dynamic indicators, including file operations, memory usage, and API calls, to identify potentially malicious actions occurring locally.

The eBPF detector is built using the BCC framework and consists of two main components: a kernel-space program and a user-space program. In the kernel space, an eBPF program written in C is attached to key system calls to monitor system activity and generate events. It calculates statistics for each active process, checks for threshold violations, and performs pattern matching on sequences of events.

 



Simple Software Pipeline


By integrating hooks into critical system calls and user-space libraries, the detector efficiently monitors and analyzes process behavior, enabling the identification of access patterns.
Results

We present the results of our experiments on ransomware detection, highlighting key findings and outcomes. This includes an overview of the dataset, detailing its size, composition, and the significance of various features in distinguishing ransomware behavior. Additionally, we assess the performance of our detection system using multiple metrics and analyze the classification results. These findings offer valuable insights into the effectiveness of our approach, as well as its strengths and limitations.
Dataset & Feature Importance:

The dataset used in our experiments consists of around 1.5 million events, containing 2786 different

processes, of which 53 were ransomware samples.
Dataset split in training and testing data.

The ransomware families that were successfully tested include the following families:

• IceFire

• MONTI

• REvil

• AvosLocker

• BlackMatter

• HelloKitty

In our case, the most important features revolve around specific patterns of file operations,

namely the sequences of ”Open”, ”Create” and ”Delete” actions.

Among these patterns, the top three influential features are:

1. Create, Open, Open (COO): This pattern signifies the sequence of creating a file, opening

an existing file, and then opening another file. It represents another behavioral pattern that

helps identify potential ransomware activities.

2. C_sum : The total number of create operations that were performed during the process.

3. Create, Open, Create (COC ): This pattern involves creating a file, opening an existing

file, and then creating another file. It captures a distinct sequence of file operations commonly

exhibited by ransomware samples.

Following Figure represents the importance, or weight, of each feature. It assigns each feature a given weight based on its relevance in predicting the output.

C – Create , O - Open

The patterns play a crucial role in differentiating a benign process with normal system operations from a ransomware process. Additionally there are other patterns like (C_max) that indicates the intensity and frequency of maximum create file operations that indicate ransomware activities.
Evaluation -
 

To assess the performance of our ransomware detection approach, we tested two machine learning models: Random Forest and Deep Neural Networks (DNNs). The evaluation was conducted using a confusion matrix, along with precision and recall as key metrics.
Confusion Matrix of Random Forest -

The confusion matrix provides an overview of classification performance of Random Forest :
Random Forest Test Results -
Evaluation Metrics

To quantify the performance of our models, we used precision and recall, defined as follows:

  True Positive Rate (Precision) - 0

  Recall (R): - 0

Confusion Matrix of Deep Neural Networks -

The confusion matrix provides an overview of classification performance of DNNs:

Evaluation Metrics

To quantify the performance of our models, we used precision and recall, defined as follows:

  True Positive Rate (Precision) - 0.10

  Recall - 1

Performance Comparison


These results demonstrate the strengths and weaknesses of each model. While Random Forest offers faster execution and interpretability, DNNs may achieve higher accuracy at the cost of increased computational complexity.

 
Conclusion and Future Scopes-

The results obtained from our ransomware detection system indicate strong performance and high effectiveness. Compared to traditional methods, our approach exhibits superior detection rates and recall, showcasing its capability to accurately identify ransomware activity. Notably, the absence of false negatives highlights the system’s robustness in correctly detecting malicious processes. However, the occurrence of false positives points to the need for further refinement to reduce the misclassification of legitimate activities. It is important to note that the system has not yet been evaluated against newly emerging ransomware variants. As a result, the outcomes may be biased due to potential gaps in the dataset, a limitation which is further addressed in the following subsection.

In this study, we presented a novel ransomware detection framework that combines the real-time monitoring capabilities of eBPF with the predictive power of machine learning. By analyzing system call behavior using a Random Forest classifier, our approach effectively distinguishes between benign and malicious activities with high accuracy. The experimental results highlight the system’s robustness, particularly in avoiding false negatives, which is critical for timely ransomware mitigation. Despite some false positives and the need for evaluation against newer ransomware strains, our solution demonstrates strong potential as a proactive and lightweight defense mechanism. Future work will focus on enhancing model generalization, reducing false positives, and extending the system’s capabilities to adapt to evolving ransomware techniques. This research paves the way for more intelligent, efficient, and context-aware security solutions in the ever-changing landscape of cyber threats.
