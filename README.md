# Bike Sharing Data Analysis Project

**Author**: Verry Kurniawan

**Email**: m200b4ky4409@bangkit.academy

**ID Dicoding**: verryk26

## Streamlit

https://verry-dicodingzzzz.streamlit.app/

## Questions to be Answered

- Pada hari apa sepeda sering dipinjam dan pada hari apa permintaan peminjaman sepeda paling sedikit?
- Pada musim mana sepeda cenderung paling populer untuk disewakan berdasarkan volume penggunaan?
- Pada jam berapa penyewaan sepeda ramai digunakan?
- Pengaruh bulan terhadap penyewaan sepeda?
- Lebih banyak mana user yang berlangganan dengan yang tidak berlangganan?

## Project Structure

- **`dashboard.py`**: This is the main Python script containing the analysis and visualizations, designed to be run via Streamlit.
- **`day.csv`**: The dataset containing daily bike rental information.
- **`hour.csv`**: The dataset containing hourly bike rental information.
- **`requirements.txt`**: Contains the necessary libraries and their versions for this project.

## Datasets

Both `hour.csv` and `day.csv` have the following fields (except for the `hr` column which is only in `hour.csv`):

- `instant`: Record index.
- `dteday`: Date.
- `season`: Season (1: spring, 2: summer, 3: fall, 4: winter).
- `yr`: Year (0: 2011, 1: 2012).
- `mnth`: Month (1 to 12).
- `hr`: Hour (0 to 23) – only in `hour.csv`.
- `holiday`: Whether the day is a holiday or not.
- `weekday`: Day of the week.
- `workingday`: 1 if the day is neither a weekend nor a holiday, otherwise 0.
- `weathersit`: Weather situation (1: Clear, 2: Mist, 3: Light Snow, 4: Heavy Rain).
- `temp`: Normalized temperature in Celsius.
- `atemp`: Normalized feeling temperature in Celsius.
- `hum`: Normalized humidity.
- `windspeed`: Normalized wind speed.
- `casual`: Count of casual users.
- `registered`: Count of registered users.
- `cnt`: Count of total rental bikes (casual + registered).

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/princeofverry/Submission_Dicoding_Verry.git
   ```

2. **Navigate to the project directory**:

   ```bash
   cd Submission_Dicoding_Verry
   ```

3. **Create a virtual environment**:

   ```bash
   virtualenv venv
   ```

4. **Activate the virtual environment**:

   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - On Mac/Linux:
     ```bash
     source venv/bin/activate
     ```

5. **Install the dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

6. **Run the Streamlit app**:
   ```bash
   streamlit run dashboard.py
   ```

## Data Cleaning Process

The following steps were taken to clean and preprocess the data:

- Eliminate columns that are not relevant or needed for the analysis.
- Rename columns to make them more descriptive and easier to understand.
- Change the data type of the `date_day` column to datetime format for time-based analysis.
- Modify the data types of specific columns to match the type of information they contain.
- Convert other data as needed to ensure consistency and readiness for further analysis.""")

## Deployment

This app is deployed on Streamlit Cloud. You can view the live version [here](verry-dicoding.streamlit.app).

## Dependencies

- Python 3.x
- pandas
- seaborn
- matplotlib
- numpy
- streamlit
