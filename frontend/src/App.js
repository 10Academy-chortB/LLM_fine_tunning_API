import React, { useState, useEffect } from 'react';
import LatestNewsDisplay from './components/LatestNewsDisplay';
import { searchNews, searchLyrics, getLatestNews } from './api'; 

const App = () => {
  const [searchInput, setSearchInput] = useState('');
  const [filter, setFilter] = useState('all'); 
  const [searchResult, setSearchResult] = useState('');
  const [loading, setLoading] = useState(false);


  const handleSearch = async () => {
    if (searchInput.trim() !== '') {
      if (filter === 'news') {
        try {
          const newsResults = await searchNews(searchInput);
          setLoading(false)
          setSearchResult(newsResults)
          console.log('News search results:', newsResults);
        } catch (error) {
          console.error('Error searching news:', error);
        }
      } else if (filter === 'lyrics') {
        // Call searchLyrics API
        try {
          console.log('dearch pressed')

          const lyricsResults = await searchLyrics(searchInput);
          setSearchResult(lyricsResults)

          console.log('Lyrics search results:', lyricsResults);
          
        } catch (error) {
          console.error('Error searching lyrics:', error);
          
        }
      } else {
      }
    }
  };
  return (
    <div className="mx-auto max-w-3xl p-6">
      <h1 className="text-4xl font-bold mb-14 mt-24">የአማርኛ መረጃ ማከማቻ</h1>
      <h2 className="text-l font-semibold mb-4">ዛሬ ምን መፈለግ ይፈልጋሉ?</h2>
      <div className="flex mb-4">
        <input
          type="text"
          placeholder="የፍለጋ ጥያቄዎን እዚህ ያስገቡ..."
          value={searchInput}
          onChange={(e) => setSearchInput(e.target.value)}
          className="flex-1 px-4 py-2 mr-2 border rounded-lg focus:outline-none focus:ring focus:border-blue-500"
        />
        <select
          value={filter}
          onChange={(e) => setFilter(e.target.value)}
          className="px-4 py-2 border rounded-lg focus:outline-none focus:ring focus:border-blue-500"
        >
          <option value="news">ዜና</option>
          <option value="lyrics">ግጥሞች</option>
        </select>
        <button
          onClick={handleSearch}
          className="px-4 py-2 ml-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600 focus:outline-none focus:ring focus:border-blue-500"
        >
          {loading ? 'መፈለግ' : 'ፈልግ'}
        </button>
      </div>
      {searchResult ? (
        <>
          <h2 className="text-xl font-bold mb-2">የፍለጋ ውጤት</h2>
          <p>{searchResult}</p>
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
        </>
      ) : (
        <>
                  <h2 className="text-xl font-bold mb-2">አዳዲስ ዜናዎች</h2>
                  <LatestNewsDisplay />
        </>
    
      )}
    </div>
  );
};

export default App;
