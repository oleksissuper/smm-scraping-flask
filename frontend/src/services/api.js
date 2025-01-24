import axios from "axios";

const API_BASE_URL = "http://127.0.0.1:5000/api";

export const fetchNetworks = async () => {
  const response = await axios.get(`${API_BASE_URL}/networks`);
  return response.data;
};

export const fetchRecords = async (requestData) => {
  try {
    const response = await axios.post(`${API_BASE_URL}/records`, requestData);
    if (response.data.status) {
      return response.data.records;
    } else {
      throw new Error(response.data.error || "Failed to fetch records");
    }
  } catch (error) {
    console.error("Error fetching records:", error);
    throw error;
  }
};
