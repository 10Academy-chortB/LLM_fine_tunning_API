import axios from 'axios';

const API_URL = 'http://localhost:5001'; // Adjust



export const searchNews = async (keyword) => {
  try {
    const response = await axios.get(`${API_URL}/news_search`, {
      params: { keyword },
    });
    return response.data;
  } catch (error) {
    console.error('Error searching news:', error);
    throw error;
  }
};

export const searchLyrics = async (keyword) => {
  try {
    const response = await axios.get(`${API_URL}/lyrics_search`, {
      params: { keyword },
    });
    return response.data;
  } catch (error) {
    console.error('Error searching lyrics:', error);
    throw error;
  }
};
export const getUniqueArtists = async () => {
    try {
      const response = await axios.get(`${API_URL}/unique_artist`);
      return response.data;
    } catch (error) {
      console.error('Error fetching unique artists:', error);
      throw error;
    }
  };
  export const getUniqueSources = async () => {
    try {
      const response = await axios.get(`${API_URL}/unique_source`);
      return response.data;
    } catch (error) {
      console.error('Error fetching unique sources:', error);
      throw error;
    }
  };
  
  export const getLatestNews = async () => {
    try {
      const response = await axios.get(`${API_URL}/latest_news`);
      return response.data;
    } catch (error) {
      console.error('Error fetching latest news:', error);
      throw error;
    }
  };
  
  
