// src/App.js
import React from 'react';
import { Routes, Route, Navigate, useLocation } from "react-router-dom";

import Home from './pages/home';
import DataView from './pages/DataView';
import routes from './routes';

const App = () => {
  const getRoutes = (allRoutes) =>
    allRoutes.map((route) => {
      if (route.collapse) {
        return getRoutes(route.collapse);
      }

      if (route.route) {
        return <Route exact path={route.route} element={route.component} key={route.key} />;
      }

      return null;
    });
  return (
    <Routes>
                {getRoutes(routes)}

        <Route path="*"  component={Home} />

    </Routes>
  );
};

export default App;
