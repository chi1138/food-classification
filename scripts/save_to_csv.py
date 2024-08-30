import os

def save_dataframe_to_csv(df, directory, filename=None, index=False):
    
    # Generate filename if not provided
    if filename is None:
        filename = "dataframe_export"
    
    # Remove .csv extension if present in the filename
    filename = filename.rsplit('.csv', 1)[0]
    
    # Construct the full file path
    file_path = os.path.join(directory, f"{filename}.csv")
    
    # Save the DataFrame to CSV
    df.to_csv(file_path, index=index)
    
    print(f"DataFrame has been saved to {file_path}")
    return file_path