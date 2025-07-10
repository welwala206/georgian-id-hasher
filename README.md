# Georgian ID Hasher

# პირადი ნომირს ანონიმიზაციის სკრიპტი

🇬🇧 For English, please scroll down

პირადი ნომერი წარმოადგენს საქართველოს მოქალაქის უნიკალურ საიდენტიფიკაციო მონაცემს, რომელიც პირს ენიჭება დაბადების რეგისტრაციის პროცესში. აღნიშნული ნომერი დატანილია მოქალაქის ოფიციალურ დოკუმენტებზე(პირადობის მოწმობა, პასპორტი, მართვის მოწმობა და სხვა). თითოეულ მოქალაქეს აქვს მხოლოდ ერთი პირადი ნომერი, ხოლო ერთი და იმავე ნომრის მინიჭება სხვადასხვა პირისთვის დაუშვებელია. ასევე დაუშვებელია უკვე მინიჭებული ნომრის შეცვლა ან გაუქმება, გარდა კანონით განსაზღვრული განსაკუთრებული შემთხვევებისა. პირადი ნომრის მინიჭების პროცესი და ყველა შესაბამისი ჩანაწერი აღირიცხება სააგენტოს მონაცემთა ბაზაში.

პირადი ნომერი შედგება თერთმეტი ციფრისაგან. მისი სტრუქტურა მოიცავს ადმინისტრაციული ერთეულის კოდს, საკონტროლო ციფრს, სააგენტოს ტერიტორიული სამსახურის კოდს და რიგით ნომერს. არსებობს სპეციალური შეზღუდვები, რომლებითაც განსაზღვრულია დაუშვებელი ციფრული კომბინაციები. საზღვარგარეთ მყოფი საქართველოს მოქალაქეებისთვის პირადი ნომრის პირველ ორ ციფრს წარმოადგენს საგარეო საქმეთა სამინისტროს კოდი, ხოლო სხვა კომპონენტები მიუთითებს შესაბამის დიპლომატიურ წარმომადგენლობასა ან საკონსულო დაწესებულებაზე.

ამგვარად, პირადი ნომერი წარმოადგენს მოქალაქის იდენტიფიცირების მთავარ საშუალებას, რომელიც უზრუნველყოფს სხვადასხვა მონაცემთა ბაზაში, საარქივო მასალებსა და სხვა ტიპის დოკუმენტაციაში პიროვნების შესახებ ინფორმაციის მოძიების ყველაზე ოპტიმალურ საშუალებას.

სამეცნიერო მიზნებისათვის შეიძლება საჭირო გახდეს, ერთი ადამიანის შესახებ არსებული მონაცემების გაერთიანება და ერთმანეთთან დაკავშირება, რომელიც ინახება სხვადასხვა ელექტრონულ მონაცემთა ბაზაში. ამავდროულად, აღნიშნული ქმედება არ უნდა უქმნიდეს ადამიანს საფრთხეს და არ ქმნიდეს კონფიდენციალურობის დარღვევის რისკს.

აღნიშნული ამოცანის გადასაჭრელად, ფართოდ არის დანერგილი კრიპტოგრაფიული ჰეშის ფუნქციის გამოყენება მონაცემთა ერთმანეთთან დასაკავშირებლად [1, 2]. იდეა მდგომარეობს იმაში, რომ ადამიანის მაიდენტიფიცირებელი უნიკალური ინფორმაციის შემცველი მონაცემი (საქართველოს შემთხვევაში - პირადი ნომერი) დამუშავდეს სპეციალური ალგორითმით და გარდაიქმნას იგვარ მონაცემად, რომელიც დარჩება უნიკალური და ამავდროულად იქნება პრაქტიკულად ანონიმური, მისი უკუ-გარდაქმნა და ადამიანის მაიდენტიფიცირებელი მონაცემის მიღება იქნება შეუძლებელი [3, 4, 5].

Python-ის სკრიპტი, დასამუშავებელ მონაცემთა ბაზაში პოულობს თერთმენტ-ნიშნა პირად ნომერს, გარდაქმნის მას შესაბამისი ალგორითმის მიხედვით და პირად ნომერს ანაცვლებს მისი ჰეშით (ე.წ. "ანონიმური კოდით"). სკრიპტი იყენებს SHA3-512 კრიპტოგრაფიული ჰეშის ფუნქცია, რომელიც პროგრამის შექმნის ეტაპზე ითვლება მოწინავე ვერსიად [6].

პროგრამას შეუძლია პირადი ნომერი დაამუშაოს ორგვარად. პირველი ვარიანტი - როდესაც ჰეშის გენერაციისათვის იყენებს მხოლოდ პირადი ნომრის მნიშვნელობას. ასეთ შემთხვევაში შეუძლებელია მიღებული ჰეშის უკუ-გარდაქმნა პირად ნომრად, მაგრამ თუ ჰეშების მონაცემების მფლობელის ხელში აღმოჩნდება რომელიმე პირადი ნომერი, მას შეუძლია იგივე ალგორითმით დაამუშაოს ის და მიღებული ჰეშის მნიშვნელობა მოძებნოს უკვე არსებულ მონაცემთა ბაზაში. ამგვარად დააკავშიროს კონკრეტული პირადი ნომრის მფლოელი ადამიანის შესახებ ინფორმაცია. აღნიშნული რისკის აღმოსაფხვრელად, შესაძლებელია მონაცემების დამუშავებიის მეორე ვარიანტის გამოყენება - როდესაც პირად ნომერთან ერთად შესაძლებელია დამატებითი ე.წ. გასაღების გამოყენება და ჰეშის მნიშვნელობა იქნება პირადი ნომრისა და გასაღების მნიშვნელობების კომბინაციით შედგენილი.

როგორც პირადი ნომერი, ასევე გასაღების მნიშვნელობები ინახება მხოლოდ მონაცემთა მფლობელთან, ხოლო მკვლევარს გადაეცემა მონაცემთა ბაზა სადაც პიროვნების საიდენტიფიკაციოდ ჩასმულია მხოლოდ ჰეში. მონაცემთა ანალიზამდე მისი ამგვარი დამუშავება შესაძლებელს ხდის მონაცემები დამუშავდეს უსაფრთხოდ.

## სკრიპტის ფუნქციები

-   ავტომატურად ამოიცნობს და ჰეშირებს 11-ციფრიან პირად ნომრებს
-   აქვს მხარდაჭერა როგორც ფაილების, ასევე დირექტორიებისათვის (ფოლდერების)
-   მუშაობს CSV და Excel (XLSX) ფორმატებთან
-   იყენებს HMAC-ს ფუნქციას მომხმარებლის მიერ მოწოდებული საიდუმლო გასაღებით (key.txt ფაილში ჩაწერილი ან სკრიპტის გაშვებისას ბრძანების ხაზში მითითებული სიტყვა)
-   მონაცემთა ბაზის დამუშავების შემდეგ ქმნის რამდენიმე ფაილს:
    -   `hashed_<ფაილის_სახელი>` — ანონიმიზებული მონაცემები
    -   `map_<ფაილის_სახელი>` — ორიგინალი და ჰეშირებული იდენტიფიკატორების შესაბამისობა (ეს ფაილი რჩება მონაცემთა მფლობელთან)
-   სკრიპტის მიერ შესრულებული ყველა მოქმედება იწერება ცალკე `file_processor.log` ფაილში

## დაწყება

### 1. პროგრამის გადმოწერა

``` bash
git clone https://github.com/welwala206/georgian-id-hasher.git
cd georgian-id-hasher
```

ასევე შესაძლებელია პროგრამის დაარქივებულ ფაილად გადმოწერა. ამისათვის, რეპოზიტორის ზედა მარჯვენა კუთხეში უნდა დააწკაპოთ მწვანე ღილაკს **Code** და გამოჩენილ მენიუში დააწყაპოთ **Download ZIP**.

### 2. სისტემის გამართვა და საჭირო ბიბლიოთეკების ინსტალაცია

სკრიპტი დაწერილია Python-ის პროგრამულ ენაზე, ამიტომ დარწმუნდით, რომ Python 3 უკვე დაყენებულია თქვენს კომპიუტერზე. ასევე, პროგრამა იყენებს Python-ის დამატებით ბიბლიოთეკებს, რომელთა ჩამონათვალიც მოცემულია ფაილში requirements.txt. დამატებითი ბიბლიოთეკების ავტობატურად ინსტალაციისათვის, შეასრულეთ ბრძანება:

``` bash
pip install -r requirements.txt
```

> Windows-ზე ასევე შესაძლებელია:
>
> ``` bash
> py -m pip install -r requirements.txt
> ```

## გამოყენება

### კოდური გასაღების მითითება

პირადი ნომრების სრულად უსაფრთხო ჰეშირებისთვის აუცილებელია გასაღების მითითება:

#### ვარიანტი 1: პირდაპირ პარამეტრით

``` bash
python main.py <ფაილის_ან_დირექტორიის_მდებარეობა> --key "თქვენი_გასაღები"
```

#### ვარიანტი 2: გასაღების ფაილით

``` bash
python main.py <ფაილის_ან_დირექტორიის_მდებარეობა> --key-file key.txt
```

> გასაღების მიუთითებლობის შემთხვევაში გამოიყენება მხოლოდ პირადი ნომრის ჰეშირება.

### მაგალითები

#### ერთი ფაილის დამუშავება

``` bash
python main.py data.xlsx --key "secureKey123"
```

#### დირექტორიაში ყველა ფაილის დამუშავება

``` bash
python main.py ./data_folder --key-file key.txt
```

## შედეგები

დამუშავების შემდეგ, დირექტორიაში შეიქმნება შემდეგი ფაილები:

-   `hashed_<ფაილის_სახელი>.csv` ან `.xlsx` — მხოლოდ ჰეშების შემცველი ფაილი
-   `map_<ფაილის_სახელი>.csv` ან `.xlsx` — ორიგინალ და ჰეშირებულ ID-ებს შორის შესაბამისობა
-   `file_processor.log` — პროგრამის მიერ შესრულებული მოქმედებების ლოგის ფაილი

## მხარდაჭერილი ოპერაციული სისტემები

| სისტემა | მხარდაჭერა |
|---------|------------|
| Windows | ✅         |
| macOS   | ✅         |
| Linux   | ✅         |

## სტრუქტურა

```         
georgian_id_hasher/
├── main.py             # ძირითადი სკრიპტი
├── requirements.txt    # საჭირო ბიბლიოთეკები
├── key.txt             # გასაღების ფაილი (არასავალდებულო)
```

## ლიცენზია

პროგრამა ვრცელდება [MIT ლიცენზიით](./LICENSE) — თავისუფლად შეგიძლიათ გამოიყენოთ, შეცვალოთ და გაავრცელოთ ციტირების მითითებით.

## დოკუმენტაციაში ციტირება

თუ პროგრამას იყენებთ კვლევებში ან პუბლიკაციებში, გთხოვთ, მიუთითოთ ციტირების შემდეგი ფორმით:

### APA-style citation

Natsvlishvili, I. (2025). Georgian ID Hasher (Version 1.0) \[Computer software\]. GitHub. https://github.com/welwala206/georgian-id-hasher

### BibTeX entry

``` latex
@misc{natsvlishvili2025georgianidhasher,
  author       = {Irakli Natsvlishvili},
  title        = {Georgian ID Hasher},
  year         = {2025},
  publisher    = {GitHub},
  journal      = {GitHub repository},
  howpublished = {\url{https://github.com/welwala206/georgian-id-hasher}},
  note         = {Accessed: 2025-07-02}
}
```

# ENGLISH VERSION

A lightweight Python utility to anonymize Georgian citizen IDs using **HMAC-SHA3-512**. This tool scans `.csv` and `.xlsx` files (or folders), detects 11-digit IDs, hashes them with a secret key, and generates anonymized files along with original-to-hashed mapping files.

## Use Case

This script is designed for **secure de-identification** of datasets containing personal identifiers (such as Georgian national IDs), ideal for:
- Health data research
- Government data processing
- Ethical data sharing

## Features

- Automatically detects and hashes **11-digit personal IDs**
- Supports **individual files** and **batch processing in folders**
- Handles both **CSV** and **Excel (.xlsx)** formats
- Uses **HMAC-SHA3-512** with user-supplied secret key
- Generates:
  - `hashed_<filename>` – anonymized dataset
  - `map_<filename>` – mapping of original → hashed IDs
- Logs all operations to `file_processor.log`

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/welwala206/georgian-id-hasher.git
cd georgian_id_hasher
```

### 2. Install Dependencies
Make sure Python 3 is installed, then run:

```bash
pip install -r requirements.txt
```

> You can also use:
> ```bash
> python -m pip install -r requirements.txt
> ```

Dependencies:
- `pandas`
- `openpyxl`
- `xlrd`

## Usage

### Providing the HMAC Key

The script supports two options for key input:
- `--key`: Pass key directly via command line
- `--key-file`: Path to a `.txt` file containing the key

### Examples

#### Process a single file:
```bash
python main.py ./data/file.xlsx --key "my_secret_key"
```

#### Process all `.csv` and `.xlsx` files in a folder:
```bash
python main.py ./data_folder --key-file key.txt
```

> If no key is provided, an empty string will be used (not secure).

## Output Files

For each input file, the script will generate:
- `hashed_<filename>.csv` or `.xlsx`: anonymized version
- `map_<filename>.csv` or `.xlsx`: original → hashed ID mapping
- `file_processor.log`: log of all actions

All files are saved in the same directory as the original.

## File Structure

```
georgian_id_hasher/
├── main.py             # Main hashing script
├── requirements.txt    # Python dependencies
├── key.txt             # Example key file
```


## Platform Compatibility

| Platform | Compatible |
|----------|------------|
| Windows  | ✅         |
| macOS    | ✅         |
| Linux    | ✅         |

## License

This project is licensed under the **MIT License**.  
You are free to use, modify, and distribute with attribution.

## Citation

If you use this tool in a publication or project, please cite:

### APA-style citation
Natsvlishvili, I. (2025). Georgian ID Hasher (Version 1.0) \[Computer software\]. GitHub. https://github.com/welwala206/georgian-id-hasher

---
# References
1. Bian, Jiang, Alexander Loiacono, Andrei Sura, Tonatiuh Mendoza Viramontes, Gloria Lipori, Yi Guo, Elizabeth Shenkman, and William Hogan. 2019. “Implementing a Hash-Based Privacy-Preserving Record Linkage Tool in the OneFlorida Clinical Research Network.” JAMIA Open 2 (4): 562–69. [https://doi.org/10.1093/jamiaopen/ooz050](https://doi.org/10.1093/jamiaopen/ooz050).
2. Tomietto, Marco, Andrew McGill, and Matthew D. Kiernan. 2023. “Implementing an Electronic Public Health Record for Policy Planning in the UK Military Sector: Validation of a Secure Hashing Algorithm.” Heliyon 9 (6): e16116. [https://doi.org/10.1016/j.heliyon.2023.e16116](https://doi.org/10.1016/j.heliyon.2023.e16116).
3. Tomietto, Marco, Andrew McGill, and Matthew D. Kiernan. 2023. “Implementing an Electronic Public Health Record for Policy Planning in the UK Military Sector: Validation of a Secure Hashing Algorithm.” Heliyon 9 (6): e16116. [https://doi.org/10.1016/j.heliyon.2023.e16116](https://doi.org/10.1016/j.heliyon.2023.e16116).
4. European Data Protection Supervisor. 2025. Introduction to the Hash Function as a Personal Data Pseudonymisation Technique | European Data Protection Supervisor. [https://www.edps.europa.eu/data-protection/our-work/publications/papers/introduction-hash-function-personal-data](https://www.edps.europa.eu/data-protection/our-work/publications/papers/introduction-hash-function-personal-data).
5. Linking with Anonymised Data How Not to Make a Hash of It. n.d. [https://www.gov.uk/government/publications/joined-up-data-in-government-the-future-of-data-linking-methods/linking-with-anonymised-data-how-not-to-make-a-hash-of-it](https://www.gov.uk/government/publications/joined-up-data-in-government-the-future-of-data-linking-methods/linking-with-anonymised-data-how-not-to-make-a-hash-of-it).
6. SHA-3. 2025. [https://en.wikipedia.org/w/index.php?title=SHA-3&oldid=1297681017](https://en.wikipedia.org/w/index.php?title=SHA-3&oldid=1297681017). 
