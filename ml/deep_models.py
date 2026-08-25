"""
PyTorch Deep Learning Architectures for Hospital Readmission Prediction
Includes Tabular ANN/MLP, Tabular Transformer, Patient Autoencoder, and Sequence LSTM.
"""

try:
    import torch
    import torch.nn as nn
    import torch.nn.functional as F
    HAS_TORCH = True
except ImportError:
    torch = None
    nn = object
    F = None
    HAS_TORCH = False

class TabularANN(nn.Module if HAS_TORCH else object):
    """Feed-Forward Neural Network for Structured Tabular Healthcare Data."""
    def __init__(self, input_dim=24, hidden_dims=[64, 32], dropout_rate=0.25):
        if HAS_TORCH:
            super(TabularANN, self).__init__()
            self.fc1 = nn.Linear(input_dim, hidden_dims[0])
            self.bn1 = nn.BatchNorm1d(hidden_dims[0])
            self.dropout1 = nn.Dropout(dropout_rate)
            self.fc2 = nn.Linear(hidden_dims[0], hidden_dims[1])
            self.bn2 = nn.BatchNorm1d(hidden_dims[1])
            self.dropout2 = nn.Dropout(dropout_rate)
            self.out = nn.Linear(hidden_dims[1], 1)

    def forward(self, x):
        # Layer 1: Dense -> BatchNorm -> ReLU -> Dropout
        x = self.fc1(x)
        if x.size(0) > 1:
            x = self.bn1(x)
        x = F.relu(x)
        x = self.dropout1(x)
        
        # Layer 2: Dense -> BatchNorm -> ReLU -> Dropout
        x = self.fc2(x)
        if x.size(0) > 1:
            x = self.bn2(x)
        x = F.relu(x)
        x = self.dropout2(x)
        
        # Output probability
        logits = self.out(x)
        return torch.sigmoid(logits)

class TabularTransformer(nn.Module):
    """Attention-Based Architecture for Tabular Healthcare EHR Data."""
    def __init__(self, num_features=24, embed_dim=32, num_heads=4, num_layers=2, dropout=0.2):
        super(TabularTransformer, self).__init__()
        self.feature_embedding = nn.Linear(1, embed_dim)
        
        encoder_layer = nn.TransformerEncoderLayer(
            d_model=embed_dim,
            nhead=num_heads,
            dim_feedforward=64,
            dropout=dropout,
            batch_first=True
        )
        self.transformer_encoder = nn.TransformerEncoder(encoder_layer, num_layers=num_layers)
        self.classifier_head = nn.Sequential(
            nn.Linear(num_features * embed_dim, 64),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(64, 1),
            nn.Sigmoid()
        )

    def forward(self, x):
        # x shape: (batch_size, num_features)
        batch_size, num_features = x.size()
        x_reshaped = x.unsqueeze(-1) # (batch_size, num_features, 1)
        embeddings = self.feature_embedding(x_reshaped) # (batch_size, num_features, embed_dim)
        
        encoded = self.transformer_encoder(embeddings)
        flattened = encoded.reshape(batch_size, -1)
        return self.classifier_head(flattened)

class PatientAutoencoder(nn.Module):
    """Autoencoder for Patient Representation, Latent Compression & Anomaly Scoring."""
    def __init__(self, input_dim=24, latent_dim=8):
        super(PatientAutoencoder, self).__init__()
        # Encoder
        self.encoder = nn.Sequential(
            nn.Linear(input_dim, 32),
            nn.ReLU(),
            nn.Linear(32, latent_dim),
            nn.ReLU()
        )
        # Decoder
        self.decoder = nn.Sequential(
            nn.Linear(latent_dim, 32),
            nn.ReLU(),
            nn.Linear(32, input_dim)
        )

    def forward(self, x):
        latent = self.encoder(x)
        reconstructed = self.decoder(latent)
        return reconstructed, latent

class PatientSequenceLSTM(nn.Module):
    """LSTM Sequence Model for Longitudinal Patient Encounters."""
    def __init__(self, input_dim=12, hidden_dim=32, num_layers=2):
        super(PatientSequenceLSTM, self).__init__()
        self.lstm = nn.LSTM(input_dim, hidden_dim, num_layers=num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_dim, 1)

    def forward(self, x):
        # x shape: (batch_size, seq_len, input_dim)
        out, (hn, cn) = self.lstm(x)
        last_step = out[:, -1, :]
        return torch.sigmoid(self.fc(last_step))
