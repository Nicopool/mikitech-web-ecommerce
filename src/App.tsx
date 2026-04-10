/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 */

import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import AdminLayout from './layouts/AdminLayout';
import StoreLayout from './layouts/StoreLayout';
import Dashboard from './pages/Dashboard';
import Store from './pages/Store';
import UserPanel from './pages/UserPanel';
import Checkout from './pages/Checkout';

export default function App() {
  return (
    <Router>
      <Routes>
        {/* Store Routes */}
        <Route element={<StoreLayout />}>
          <Route path="/" element={<Store />} />
          <Route path="/panel" element={<UserPanel />} />
          <Route path="/checkout" element={<Checkout />} />
        </Route>

        {/* Admin Routes */}
        <Route path="/admin" element={<AdminLayout />}>
          <Route index element={<Dashboard />} />
          {/* Add more admin routes here if needed */}
        </Route>
      </Routes>
    </Router>
  );
}

