"""Supabase client initialization and utilities."""
import os

try:
    from supabase import create_client
    SUPABASE_AVAILABLE = True
except ImportError:
    SUPABASE_AVAILABLE = False


def get_supabase_client():
    """
    Initialize and return a Supabase client.
    
    Returns:
        supabase.client.Client: Authenticated Supabase client, or None if not available
    
    Requires SUPABASE_URL and SUPABASE_KEY environment variables.
    """
    if not SUPABASE_AVAILABLE:
        raise ImportError(
            "supabase-py is not installed. Install it with: pip install supabase"
        )
    
    url = os.getenv('SUPABASE_URL')
    key = os.getenv('SUPABASE_KEY')
    
    if not url or not key:
        raise ValueError(
            "SUPABASE_URL and SUPABASE_KEY environment variables must be set"
        )
    
    return create_client(url, key)


# Lazy initialization: only create client when needed
_supabase_client = None


def supabase():
    """Get cached Supabase client instance."""
    global _supabase_client
    if _supabase_client is None:
        _supabase_client = get_supabase_client()
    return _supabase_client
