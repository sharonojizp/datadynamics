import os
import psutil
import json
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DataDynamics:
    def __init__(self, directory):
        self.directory = directory
        self.data_summary = {}

    def analyze_storage(self):
        logging.info(f"Starting storage analysis in directory: {self.directory}")
        for root, dirs, files in os.walk(self.directory):
            for file in files:
                file_path = os.path.join(root, file)
                file_size = os.path.getsize(file_path)
                self.data_summary[file_path] = file_size
        logging.info("Completed storage analysis.")

    def suggest_optimization(self):
        logging.info("Suggesting optimizations based on storage analysis.")
        total_size = sum(self.data_summary.values())
        logging.info(f"Total size of files: {total_size} bytes")

        # Simulate a simple optimization suggestion based on file size
        optimization_suggestions = []
        for file_path, file_size in self.data_summary.items():
            if file_size > 10485760:  # 10 MB
                optimization_suggestions.append(f"Consider compressing {file_path}")

        return optimization_suggestions

    def save_analysis(self, output_file):
        with open(output_file, 'w') as f:
            json.dump(self.data_summary, f, indent=4)
        logging.info(f"Analysis saved to {output_file}")

    def get_system_memory_info(self):
        memory_info = psutil.virtual_memory()
        logging.info(f"Total memory: {memory_info.total}")
        logging.info(f"Available memory: {memory_info.available}")
        return memory_info

if __name__ == "__main__":
    directory_to_analyze = "C:\\Your\\Directory\\Path"
    output_file_path = "storage_analysis.json"

    dd = DataDynamics(directory_to_analyze)
    dd.analyze_storage()
    suggestions = dd.suggest_optimization()
    dd.save_analysis(output_file_path)
    memory_info = dd.get_system_memory_info()

    logging.info("Optimization Suggestions:")
    for suggestion in suggestions:
        logging.info(suggestion)