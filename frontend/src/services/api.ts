import axios from "axios";

const API_BASE_URL = "http://localhost:8000/api/v1";

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    "Content-Type": "application/json",
  },
});

// Income API
export interface Income {
  id: string;
  amount: number;
  category: string;
  description?: string;
  date: string;
  created_at: string;
  updated_at: string;
}

export interface IncomeCreate {
  amount: number;
  category: string;
  description?: string;
  date: string;
}

export const incomeAPI = {
  getAll: () => api.get<Income[]>("/incomes"),
  getById: (id: string) => api.get<Income>(`/incomes/${id}`),
  create: (data: IncomeCreate) => api.post<string>("/incomes", data),
  update: (id: string, data: IncomeCreate) =>
    api.put<Income>(`/incomes/${id}`, data),
  delete: (id: string) => api.delete(`/incomes/${id}`),
};

// Expense API
export interface Expense {
  id: string;
  amount: number;
  category: string;
  description?: string;
  date: string;
  created_at: string;
  updated_at: string;
}

export interface ExpenseCreate {
  amount: number;
  category: string;
  description?: string;
  date: string;
}

export const expenseAPI = {
  getAll: () => api.get<Expense[]>("/expenses"),
  getById: (id: string) => api.get<Expense>(`/expenses/${id}`),
  create: (data: ExpenseCreate) => api.post<string>("/expenses", data),
  update: (id: string, data: ExpenseCreate) =>
    api.put<Expense>(`/expenses/${id}`, data),
  delete: (id: string) => api.delete(`/expenses/${id}`),
};

export default api;
