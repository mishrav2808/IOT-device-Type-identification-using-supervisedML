# IOT-device-Type-identification-using-supervised-ML
Iot devices are relatively new, therefore their software assurance may
not be present, and they may be vulnerable to vulnerabilities. making
them typically the weakest link in a corporate network. Cybersecurity
teams need additional technology to keep track of all the devices and
keep the network safe. A machine learning (ML) approach to IoT
security can address some of these challenges. It solves the issue of
identifying unknown devices on a network, ensuring they're included in
the existing security framework and makes IoT management easier for
busy IT teams. The first step is to identify these devices. For this ,
several pcap files with  a lot of packet entries of seven D-Link IoT
Devices each .Those packets with TCP protocol were filtered out and a
single pcap file for each device was made and it was named with name
of the device it belonged to ,then those names were taken as labels
and features from all those files were extracted to obtain a single
vector space matrix and that was used to train 4 different machine
learning model namely logistic Regression, Random Forest, Decision
Tree and Naive Bayes out of which Decision Tree predicted the device
type with best accuracy of 96%.
