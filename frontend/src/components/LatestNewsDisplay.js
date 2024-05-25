import React, { useEffect, useState } from 'react';
import { getLatestNews } from '../api';

const LatestNewsDisplay = () => {
  const [latestNews, setLatestNews] = useState([]);
  
  useEffect(() => {
    const fetchLatestNews = async () => {
      try {
        const news = await getLatestNews();
        setLatestNews(news);
      } catch (error) {
        console.error('Error fetching latest news:', error);
      }
    };

    fetchLatestNews(); // Execute the function
  }, []);
  
  return (
    <div className="grid gap-4 ">
      {/* {latestNews} */}
      <div className="border border-gray-300 rounded-lg p-4">
          <h3 className="font-semibold mb-2">{ 'Title'}</h3>
          <p className="text-sm mb-2">{ '"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."'}</p>
          <div className="flex justify-between text-xs">
            <p>{'03/03/2024'}</p>
            <p>{ 'Source : Tikvah'}</p>
          </div>
        </div>
        <div className="border border-gray-300 rounded-lg p-4">
          <h3 className="font-semibold mb-2">{ 'Title'}</h3>
          <p className="text-sm mb-2">{ '"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."'}</p>
          <div className="flex justify-between text-xs">
            <p>{'03/03/2024'}</p>
            <p>{ 'Source : Tikvah'}</p>
          </div>
        </div>

      {/* {latestNews.map((newsItem, index) => (
        <div key={index} className="border border-gray-300 rounded-lg p-4">
          <h3 className="font-semibold mb-2">{newsItem.title || 'Title Placeholder'}</h3>
          <p className="text-sm mb-2">{newsItem.content || 'Content Placeholder'}</p>
          <div className="flex justify-between text-xs">
            <p>{newsItem.date || 'Date Placeholder'}</p>
            <p>{newsItem.source || 'Source Placeholder'}</p>
          </div>
        </div>
      ))} */}
    </div>
  );
};

export default LatestNewsDisplay;
