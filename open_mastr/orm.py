from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import MetaData
from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    Sequence,
    DateTime,
    Boolean,
    func,
    Date,
    JSON,
)
import os

DB_ENGINE = os.environ.get("DB_ENGINE", "sqlite")


mirror_schema = "mastr_mirrored" if DB_ENGINE == "docker" else None
meta = MetaData(schema=mirror_schema)
Base = declarative_base(metadata=meta)


class ParentAllTables(object):

    DatenQuelle = Column(String)
    DatumDownload = Column(Date)


class BasicUnit(Base):
    __tablename__ = "basic_units"

    EinheitMastrNummer = Column(String, primary_key=True)
    DatumLetzteAktualisierung = Column(DateTime(timezone=True))
    Name = Column(String)
    Einheitart = Column(String)
    Einheittyp = Column(String)
    Standort = Column(String)
    Bruttoleistung = Column(Float)
    Erzeugungsleistung = Column(Float)
    EinheitBetriebsstatus = Column(String)
    Anlagenbetreiber = Column(String)
    EegMastrNummer = Column(String)
    KwkMastrNummer = Column(String)
    SpeMastrNummer = Column(String)
    GenMastrNummer = Column(String)
    BestandsanlageMastrNummer = Column(String)
    NichtVorhandenInMigriertenEinheiten = Column(String)
    StatisikFlag = Column(String)


class AdditionalDataRequested(Base):
    __tablename__ = "additional_data_requested"

    id = Column(
        Integer,
        Sequence("additional_data_requested_id_seq", schema=mirror_schema),
        primary_key=True,
    )
    EinheitMastrNummer = Column(String)
    additional_data_id = Column(String)
    technology = Column(String)
    data_type = Column(String)
    request_date = Column(DateTime(timezone=True), default=func.now())


class MissedAdditionalData(Base):
    __tablename__ = "missed_additional_data"

    id = Column(
        Integer,
        Sequence("additional_data_missed_id_seq", schema=mirror_schema),
        primary_key=True,
    )
    additional_data_id = Column(String)
    reason = Column(String)
    download_date = Column(DateTime(timezone=True), default=func.now())


class Extended(object):

    NetzbetreiberMastrNummer = Column(String)
    Registrierungsdatum = Column(Date)
    EinheitMastrNummer = Column(String, primary_key=True)
    DatumLetzteAktualisierung = Column(DateTime(timezone=True))
    LokationMastrNummer = Column(String)
    NetzbetreiberpruefungStatus = Column(String)
    NetzbetreiberpruefungDatum = Column(Date)
    AnlagenbetreiberMastrNummer = Column(String)
    Land = Column(String)
    Bundesland = Column(String)
    Landkreis = Column(String)
    Gemeinde = Column(String)
    Gemeindeschluessel = Column(String)
    Postleitzahl = Column(String)
    Gemarkung = Column(String)
    FlurFlurstuecknummern = Column(String)
    Strasse = Column(String)
    StrasseNichtGefunden = Column(Boolean)
    Hausnummer = Column(String)
    HausnummerNichtGefunden = Column(Boolean)
    Adresszusatz = Column(String)
    Ort = Column(String)
    Laengengrad = Column(String) if DB_ENGINE == "docker" else Column(Float)
    Breitengrad = Column(String) if DB_ENGINE == "docker" else Column(Float)
    UtmZonenwert = Column(String)
    UtmEast = Column(String) if DB_ENGINE == "docker" else Column(Float)
    UtmNorth = Column(String) if DB_ENGINE == "docker" else Column(Float)
    GaussKruegerHoch = Column(String) if DB_ENGINE == "docker" else Column(Float)
    GaussKruegerRechts = Column(String) if DB_ENGINE == "docker" else Column(Float)
    Meldedatum = Column(Date)
    GeplantesInbetriebnahmedatum = Column(Date)
    Inbetriebnahmedatum = Column(Date)
    DatumEndgueltigeStilllegung = Column(Date)
    DatumBeginnVoruebergehendeStilllegung = Column(Date)
    DatumBeendigungVorlaeufigenStilllegung = Column(Date)
    DatumWiederaufnahmeBetrieb = Column(Date)
    EinheitSystemstatus = Column(String)
    EinheitBetriebsstatus = Column(String)
    BestandsanlageMastrNummer = Column(String)
    NichtVorhandenInMigriertenEinheiten = Column(Boolean)
    AltAnlagenbetreiberMastrNummer = Column(String)
    DatumDesBetreiberwechsels = Column(Date)
    DatumRegistrierungDesBetreiberwechsels = Column(Date)
    StatisikFlag = Column(String)
    NameStromerzeugungseinheit = Column(String)
    Weic = Column(String)
    WeicDisplayName = Column(String)
    Kraftwerksnummer = Column(String)
    Energietraeger = Column(String)
    Bruttoleistung = Column(Float)
    Nettonennleistung = Column(Float)
    AnschlussAnHoechstOderHochSpannung = Column(Boolean)
    Schwarzstartfaehigkeit = Column(Boolean)
    Inselbetriebsfaehigkeit = Column(Boolean)
    Einsatzverantwortlicher = Column(String)
    FernsteuerbarkeitNb = Column(Boolean)
    FernsteuerbarkeitDv = Column(Boolean)
    FernsteuerbarkeitDr = Column(Boolean)
    Einspeisungsart = Column(String)
    PraequalifiziertFuerRegelenergie = Column(Boolean)
    GenMastrNummer = Column(String)
    # from bulk download
    Hausnummer_nv = Column(Boolean)
    Weic_nv = Column(Boolean)
    Kraftwerksnummer_nv = Column(Boolean)
    NichtVorhandenInMigriertenEinheiten = Column(Boolean)
    Einsatzverantwortlicher = Column(String)


class WindExtended(Extended, ParentAllTables, Base):
    __tablename__ = "wind_extended"

    # wind specific attributes
    NameWindpark = Column(String)
    Lage = Column(String)
    Seelage = Column(String)
    ClusterOstsee = Column(String)
    ClusterNordsee = Column(String)
    Hersteller = Column(String)
    HerstellerId = Column(String)
    Technologie = Column(String)
    Typenbezeichnung = Column(String)
    Nabenhoehe = Column(Float)
    Rotordurchmesser = Column(Float)
    Rotorblattenteisungssystem = Column(Boolean)
    AuflageAbschaltungLeistungsbegrenzung = Column(Boolean)
    AuflagenAbschaltungSchallimmissionsschutzNachts = Column(Boolean)
    AuflagenAbschaltungSchallimmissionsschutzTagsueber = Column(Boolean)
    AuflagenAbschaltungSchattenwurf = Column(Boolean)
    AuflagenAbschaltungTierschutz = Column(Boolean)
    AuflagenAbschaltungEiswurf = Column(Boolean)
    AuflagenAbschaltungSonstige = Column(Boolean)
    Wassertiefe = Column(Float)
    Kuestenentfernung = Column(Float)
    EegMastrNummer = Column(String)


class SolarExtended(Extended, ParentAllTables, Base):
    __tablename__ = "solar_extended"

    zugeordneteWirkleistungWechselrichter = Column(Float)
    GemeinsamerWechselrichterMitSpeicher = Column(String)
    AnzahlModule = Column(Integer)
    Lage = Column(String)
    Leistungsbegrenzung = Column(String)
    EinheitlicheAusrichtungUndNeigungswinkel = Column(Boolean)
    Hauptausrichtung = Column(String)
    HauptausrichtungNeigungswinkel = Column(String)
    Nebenausrichtung = Column(String)
    NebenausrichtungNeigungswinkel = Column(String)
    InAnspruchGenommeneFlaeche = Column(Float)
    ArtDerFlaeche = Column(String)
    InAnspruchGenommeneAckerflaeche = Column(Float)
    Nutzungsbereich = Column(String)
    EegMastrNummer = Column(String)
    ArtDerFlaecheIds = Column(String)


class BiomassExtended(Extended, ParentAllTables, Base):
    __tablename__ = "biomass_extended"

    Hauptbrennstoff = Column(String)
    Biomasseart = Column(String)
    Technologie = Column(String)
    EegMastrNummer = Column(String)
    KwkMastrNummer = Column(String)


class CombustionExtended(Extended, ParentAllTables, Base):
    __tablename__ = "combustion_extended"

    NameKraftwerk = Column(String)
    NameKraftwerksblock = Column(String)
    DatumBaubeginn = Column(Date)
    AnzeigeEinerStilllegung = Column(Boolean)
    ArtDerStilllegung = Column(String)
    DatumBeginnVorlaeufigenOderEndgueltigenStilllegung = Column(Date)
    SteigerungNettonennleistungKombibetrieb = Column(Float)
    AnlageIstImKombibetrieb = Column(Boolean)
    MastrNummernKombibetrieb = Column(String)
    NetzreserveAbDatum = Column(Date)
    SicherheitsbereitschaftAbDatum = Column(Date)
    Hauptbrennstoff = Column(String)
    WeitererHauptbrennstoff = Column(String)
    WeitereBrennstoffe = Column(String)
    VerknuepfteErzeugungseinheiten = Column(String)
    BestandteilGrenzkraftwerk = Column(Boolean)
    NettonennleistungDeutschland = Column(Float)
    AnteiligNutzungsberechtigte = Column(String)
    Notstromaggregat = Column(Boolean)
    Einsatzort = Column(String)
    KwkMastrNummer = Column(String)
    Technologie = Column(String)


class GsgkExtended(Extended, ParentAllTables, Base):
    __tablename__ = "gsgk_extended"

    Technologie = Column(String)
    KwkMastrNummer = Column(String)
    EegMastrNummer = Column(String)


class HydroExtended(Extended, ParentAllTables, Base):
    __tablename__ = "hydro_extended"

    NameKraftwerk = Column(String)
    ArtDerWasserkraftanlage = Column(String)
    AnzeigeEinerStilllegung = Column(Boolean)
    ArtDerStilllegung = Column(String)
    DatumBeginnVorlaeufigenOderEndgueltigenStilllegung = Column(Date)
    MinderungStromerzeugung = Column(Boolean)
    BestandteilGrenzkraftwerk = Column(Boolean)
    NettonennleistungDeutschland = Column(Float)
    ArtDesZuflusses = Column(String)
    EegMastrNummer = Column(String)


class NuclearExtended(Extended, ParentAllTables, Base):
    __tablename__ = "nuclear_extended"

    NameKraftwerk = Column(String)
    NameKraftwerksblock = Column(String)
    Technologie = Column(String)


class StorageExtended(Extended, ParentAllTables, Base):
    __tablename__ = "storage_extended"

    Einsatzort = Column(String)
    AcDcKoppelung = Column(String)
    Batterietechnologie = Column(String)
    PumpbetriebLeistungsaufnahme = Column(Float)
    PumpbetriebKontinuierlichRegelbar = Column(Boolean)
    Pumpspeichertechnologie = Column(String)
    Notstromaggregat = Column(Boolean)
    BestandteilGrenzkraftwerk = Column(Boolean)
    NettonennleistungDeutschland = Column(Float)
    ZugeordnenteWirkleistungWechselrichter = Column(Float)
    NutzbareSpeicherkapazitaet = Column(Float)
    SpeMastrNummer = Column(String)
    EegMastrNummer = Column(String)
    EegAnlagentyp = Column(String)
    Technologie = Column(String)


class Eeg(object):

    Registrierungsdatum = Column(Date)
    EegMastrNummer = Column(String, primary_key=True)
    Meldedatum = Column(Date)
    DatumLetzteAktualisierung = Column(DateTime(timezone=True))
    EegInbetriebnahmedatum = Column(Date)
    VerknuepfteEinheit = Column(String)


class WindEeg(Eeg, ParentAllTables, Base):
    __tablename__ = "wind_eeg"

    AnlagenkennzifferAnlagenregister = Column(String)
    AnlagenschluesselEeg = Column(String)
    PrototypAnlage = Column(Boolean)
    PilotAnlage = Column(Boolean)
    InstallierteLeistung = Column(Float)
    VerhaeltnisErtragsschaetzungReferenzertrag = Column(Float)
    VerhaeltnisReferenzertragErtrag5Jahre = Column(Float)
    VerhaeltnisReferenzertragErtrag10Jahre = Column(Float)
    VerhaeltnisReferenzertragErtrag15Jahre = Column(Float)
    AusschreibungZuschlag = Column(Boolean)
    Zuschlagsnummer = Column(String)
    AnlageBetriebsstatus = Column(String)
    AnlagenkennzifferAnlagenregister_nv = Column(Boolean)
    VerhaeltnisErtragsschaetzungReferenzertrag_nv = Column(Boolean)
    VerhaeltnisReferenzertragErtrag5Jahre_nv = Column(Boolean)
    VerhaeltnisReferenzertragErtrag10Jahre_nv = Column(Boolean)
    VerhaeltnisReferenzertragErtrag15Jahre_nv = Column(Boolean)


class SolarEeg(Eeg, ParentAllTables, Base):
    __tablename__ = "solar_eeg"

    InanspruchnahmeZahlungNachEeg = Column(Boolean)
    AnlagenschluesselEeg = Column(String)
    AnlagenkennzifferAnlagenregister = Column(String)
    InstallierteLeistung = Column(Float)
    RegistrierungsnummerPvMeldeportal = Column(String)
    MieterstromRegistrierungsdatum = Column(Date)
    MieterstromZugeordnet = Column(Boolean)
    MieterstromMeldedatum = Column(Date)
    MieterstromErsteZuordnungZuschlag = Column(Date)
    AusschreibungZuschlag = Column(Boolean)
    ZugeordneteGebotsmenge = Column(Float)
    Zuschlagsnummer = Column(String)
    AnlageBetriebsstatus = Column(String)
    AnlagenkennzifferAnlagenregister_nv = Column(Boolean)
    RegistrierungsnummerPvMeldeportal_nv = Column(Boolean)


class BiomassEeg(Eeg, ParentAllTables, Base):
    __tablename__ = "biomass_eeg"

    AnlagenschluesselEeg = Column(String)
    AnlagenkennzifferAnlagenregister = Column(String)
    InstallierteLeistung = Column(Float)
    AusschliesslicheVerwendungBiomasse = Column(Boolean)
    AusschreibungZuschlag = Column(Boolean)
    Zuschlagsnummer = Column(String)
    BiogasInanspruchnahmeFlexiPraemie = Column(Boolean)
    BiogasDatumInanspruchnahmeFlexiPraemie = Column(Date)
    BiogasLeistungserhoehung = Column(Boolean)
    BiogasDatumLeistungserhoehung = Column(Date)
    BiogasUmfangLeistungserhoehung = Column(Float)
    BiogasGaserzeugungskapazitaet = Column(Float)
    BiogasHoechstbemessungsleistung = Column(Float)
    BiomethanErstmaligerEinsatz = Column(Date)
    AnlageBetriebsstatus = Column(String)
    AnlagenkennzifferAnlagenregister_nv = Column(Boolean)
    BiogasGaserzeugungskapazitaet_nv = Column(Boolean)
    BiomethanErstmaligerEinsatz_nv = Column(Boolean)


class GsgkEeg(Eeg, ParentAllTables, Base):
    __tablename__ = "gsgk_eeg"

    AnlagenschluesselEeg = Column(String)
    AnlagenkennzifferAnlagenregister = Column(String)
    InstallierteLeistung = Column(Float)
    AnlageBetriebsstatus = Column(String)
    AnlagenkennzifferAnlagenregister_nv = Column(Boolean)


class HydroEeg(Eeg, ParentAllTables, Base):
    __tablename__ = "hydro_eeg"

    AnlagenschluesselEeg = Column(String)
    AnlagenkennzifferAnlagenregister = Column(String)
    InstallierteLeistung = Column(Float)
    AnlageBetriebsstatus = Column(String)
    Ertuechtigung = Column(JSON)
    AnlagenkennzifferAnlagenregister_nv = Column(Boolean)
    ErtuechtigungIds = Column(String)


class StorageEeg(Eeg, ParentAllTables, Base):
    __tablename__ = "storage_eeg"


class Kwk(ParentAllTables, Base):
    __tablename__ = "kwk"

    Registrierungsdatum = Column(Date)
    KwkMastrNummer = Column(String, primary_key=True)
    AusschreibungZuschlag = Column(Boolean)
    Zuschlagnummer = Column(String)
    DatumLetzteAktualisierung = Column(DateTime(timezone=True))
    Inbetriebnahmedatum = Column(Date)
    Meldedatum = Column(Date)
    ThermischeNutzleistung = Column(Float)
    ElektrischeKwkLeistung = Column(Float)
    VerknuepfteEinheiten = Column(String)
    AnlageBetriebsstatus = Column(String)


class Permit(ParentAllTables, Base):
    __tablename__ = "permit"

    Registrierungsdatum = Column(Date)
    GenMastrNummer = Column(String, primary_key=True)
    DatumLetzteAktualisierung = Column(DateTime(timezone=True))
    Art = Column(String)
    Datum = Column(Date)
    Behoerde = Column(String)
    Aktenzeichen = Column(String)
    Frist = Column(Date)
    WasserrechtsNummer = Column(String)
    WasserrechtAblaufdatum = Column(Date)
    Meldedatum = Column(Date)
    VerknuepfteEinheiten = Column(String)
    Frist_nv = Column(Boolean)
    WasserrechtAblaufdatum_nv = Column(Boolean)


class LocationBasic(ParentAllTables, Base):
    __tablename__ = "locations_basic"

    LokationMastrNummer = Column(String, primary_key=True)
    NameDerTechnischenLokation = Column(String)
    Lokationtyp = Column(String)
    AnzahlNetzanschlusspunkte = Column(Integer)


class LocationExtended(ParentAllTables, Base):
    __tablename__ = "locations_extended"

    MastrNummer = Column(String, primary_key=True)
    DatumLetzteAktualisierung = Column(DateTime(timezone=True))
    NameDerTechnischenLokation = Column(String)
    VerknuepfteEinheiten = Column(JSONB) if DB_ENGINE == "docker" else Column(JSON)
    Netzanschlusspunkte = Column(JSONB) if DB_ENGINE == "docker" else Column(JSON)
    Lokationtyp = Column(String)


class AdditionalLocationsRequested(ParentAllTables, Base):
    __tablename__ = "additional_locations_requested"

    id = Column(
        Integer,
        Sequence("additional_locations_requested_id_seq", schema=mirror_schema),
        primary_key=True,
    )
    LokationMastrNummer = Column(String)
    location_type = Column(String)
    request_date = Column(DateTime(timezone=True), default=func.now())


class MissedExtendedLocation(ParentAllTables, Base):
    __tablename__ = "missed_extended_location_data"

    id = Column(
        Integer,
        Sequence("additional_location_data_missed_id_seq", schema=mirror_schema),
        primary_key=True,
    )
    LokationMastrNummer = Column(String)
    reason = Column(String)
    download_date = Column(DateTime(timezone=True), default=func.now())


class GasStorage(ParentAllTables, Base):
    __tablename__ = "gas_storage"

    MaStRNummer = Column(String, primary_key=True)
    DatumLetzteAktualisierung = Column(DateTime(timezone=True))
    Speichername = Column(String)
    Registrierungsdatum = Column(Date)
    AnlageBetriebsstatus = Column(String)
    VerknuepfteEinheit = Column(String)


class GasStorageExtended(ParentAllTables, Base):
    __tablename__ = "gas_storage_extended"
    EinheitMastrNummer = Column(String, primary_key=True)
    DatumLetzteAktualisierung = Column(DateTime(timezone=True))
    LokationMaStRNummer = Column(String)
    NetzbetreiberpruefungStatus = Column(Boolean)
    NetzbetreiberpruefungDatum = Column(Date)
    AnlagenbetreiberMastrNummer = Column(String)
    Land = Column(String)
    Bundesland = Column(String)
    Landkreis = Column(String)
    Gemeinde = Column(String)
    Gemeindeschluessel = Column(String)
    Postleitzahl = Column(Integer)
    Ort = Column(String)
    Strasse = Column(String)
    StrasseNichtGefunden = Column(Integer)
    Hausnummer = Column(String)
    Hausnummer_nv = Column(Integer)
    HausnummerNichtGefunden = Column(Integer)
    Laengengrad = Column(Float)
    Breitengrad = Column(Float)
    Registrierungsdatum = Column(String)
    Inbetriebnahmedatum = Column(String)
    EinheitSystemstatus = Column(String)
    EinheitBetriebsstatus = Column(String)
    NichtVorhandenInMigriertenEinheiten = Column(Integer)
    NameGasspeicher = Column(String)
    Speicherart = Column(String)
    MaximalNutzbaresArbeitsgasvolumen = Column(Float)
    MaximaleEinspeicherleistung = Column(Float)
    MaximaleAusspeicherleistung = Column(Float)
    DurchschnittlicherBrennwert = Column(Float)
    Weic = Column(String)
    Weic_Na = Column(Integer)
    SpeicherMaStRNummer = Column(String)
    Gemarkung = Column(String)
    FlurFlurstuecknummern = Column(String)
    Adresszusatz = Column(String)
    DatumBeginnVoruebergehendeStilllegung = Column(Date)


class StorageUnits(ParentAllTables, Base):
    __tablename__ = "storage_units"
    MaStRNummer = Column(String, primary_key=True)
    Registrierungsdatum = Column(Date)
    DatumLetzteAktualisierung = Column(DateTime(timezone=True))
    NutzbareSpeicherkapazitaet = Column(Float)
    VerknuepfteEinheit = Column(String)
    AnlageBetriebsstatus = Column(String)


class BalancingArea(ParentAllTables, Base):
    __tablename__ = "balancing_area"

    Id = Column(Integer, primary_key=True)
    Yeic = Column(String)
    RegelzoneNetzanschlusspunkt = Column(String)
    BilanzierungsgebietNetzanschlusspunkt = Column(String)


class GasProducer(ParentAllTables, Base):
    __tablename__ = "gas_producer"

    EinheitMaStRNummer = Column(String, primary_key=True)
    DatumLetzteAktualisierung = Column(DateTime(timezone=True))
    LokationMaStRNummer = Column(String)
    NetzbetreiberpruefungStatus = Column(Boolean)
    NetzbetreiberpruefungDatum = Column(Date)
    AnlagenbetreiberMastrNummer = Column(String)
    Land = Column(String)
    Bundesland = Column(String)
    Landkreis = Column(String)
    Gemeinde = Column(String)
    Gemeindeschluessel = Column(String)
    Postleitzahl = Column(Integer)
    Ort = Column(String)
    Registrierungsdatum = Column(Date)
    Inbetriebnahmedatum = Column(Date)
    EinheitSystemstatus = Column(String)
    EinheitBetriebsstatus = Column(String)
    NichtVorhandenInMigriertenEinheiten = Column(Integer)
    NameGaserzeugungseinheit = Column(String)
    SpeicherMaStRNummer = Column(String)
    Strasse = Column(String)
    StrasseNichtGefunden = Column(Integer)
    Hausnummer = Column(String)
    Hausnummer_nv = Column(Integer)
    HausnummerNichtGefunden = Column(Integer)
    Adresszusatz = Column(String)
    Laengengrad = Column(Float)
    Breitengrad = Column(Float)
    Technologie = Column(String)
    Erzeugungsleistung = Column(Float)
    DatumDesBetreiberwechsels = Column(Date)
    DatumRegistrierungDesBetreiberwechsels = Column(Date)
    Gemarkung = Column(String)
    FlurFlurstuecknummern = Column(String)
    GeplantesInbetriebnahmedatum = Column(Date)
    DatumBeginnVoruebergehendeStilllegung = Column(Date)


class GasConsumer(ParentAllTables, Base):
    __tablename__ = "gas_consumer"

    EinheitMaStRNummer = Column(String, primary_key=True)
    DatumLetzteAktualisierung = Column(DateTime(timezone=True))
    LokationMaStRNummer = Column(String)
    NetzbetreiberpruefungStatus = Column(Boolean)
    NetzbetreiberpruefungDatum = Column(Date)
    AnlagenbetreiberMastrNummer = Column(String)
    Land = Column(String)
    Bundesland = Column(String)
    Landkreis = Column(String)
    Gemeinde = Column(String)
    Gemeindeschluessel = Column(String)
    Postleitzahl = Column(Integer)
    Ort = Column(String)
    Strasse = Column(String)
    StrasseNichtGefunden = Column(Integer)
    Hausnummer = Column(String)
    Hausnummer_nv = Column(Integer)
    HausnummerNichtGefunden = Column(Integer)
    Laengengrad = Column(Float)
    Breitengrad = Column(Float)
    Registrierungsdatum = Column(String)
    Inbetriebnahmedatum = Column(String)
    EinheitSystemstatus = Column(String)
    EinheitBetriebsstatus = Column(String)
    NichtVorhandenInMigriertenEinheiten = Column(Integer)
    NameGasverbrauchsseinheit = Column(String)
    EinheitDientDerStromerzeugung = Column(String)
    MaximaleGasbezugsleistung = Column(Float)
    VerknuepfteEinheit = Column(String)
    GeplantesInbetriebnahmedatum = Column(Date)
    Adresszusatz = Column(String)
    Gemarkung = Column(String)
    FlurFlurstuecknummern = Column(String)
    DatumDesBetreiberwechsels = Column(Date)
    DatumRegistrierungDesBetreiberwechsels = Column(Date)
    DatumEndgueltigeStilllegung = Column(Date)
    DatumBeginnVoruebergehendeStilllegung = Column(Date)


class ElectricityConsumer(ParentAllTables, Base):
    __tablename__ = "electricity_consumer"

    EinheitMaStRNummer = Column(String, primary_key=True)
    DatumLetzteAktualisierung = Column(DateTime(timezone=True))
    LokationMaStRNummer = Column(String)
    NetzbetreiberpruefungStatus = Column(Boolean)
    NetzbetreiberpruefungDatum = Column(Date)
    AnlagenbetreiberMastrNummer = Column(String)
    Land = Column(String)
    Bundesland = Column(String)
    Landkreis = Column(String)
    Gemeinde = Column(String)
    Gemeindeschluessel = Column(String)
    Postleitzahl = Column(Integer)
    Ort = Column(String)
    Strasse = Column(String)
    StrasseNichtGefunden = Column(Integer)
    Hausnummer = Column(String)
    Hausnummer_nv = Column(Integer)
    HausnummerNichtGefunden = Column(Integer)
    Adresszusatz = Column(String)
    Gemarkung = Column(String)
    FlurFlurstuecknummern = Column(String)
    Laengengrad = Column(Float)
    Breitengrad = Column(Float)
    Registrierungsdatum = Column(String)
    Inbetriebnahmedatum = Column(String)
    EinheitSystemstatus = Column(String)
    EinheitBetriebsstatus = Column(String)
    NichtVorhandenInMigriertenEinheiten = Column(Integer)
    Einsatzverantwortlicher = Column(String)
    NameStromverbrauchseinheit = Column(String)
    AnzahlStromverbrauchseinheitenGroesser50Mw = Column(Integer)
    PraequalifiziertGemaessAblav = Column(Boolean)
    AnteilBeinflussbareLast = Column(Float)
    ArtAbschaltbareLast = Column(String)
    DatumDesBetreiberwechsels = Column(Date)
    DatumRegistrierungDesBetreiberwechsels = Column(Date)
    DatumEndgueltigeStilllegung = Column(Date)
    GeplantesInbetriebnahmedatum = Column(Date)


class MarketRoles(ParentAllTables, Base):
    __tablename__ = "market_roles"

    MastrNummer = Column(String, primary_key=True)
    MarktakteurMastrNummer = Column(String)
    Marktrolle = Column(String)
    Marktpartneridentifikationsnummer_nv = Column(Boolean)
    BundesnetzagenturBetriebsnummer = Column(String)
    BundesnetzagenturBetriebsnummer_nv = Column(Boolean)
    Marktpartneridentifikationsnummer = Column(String)
    KontaktdatenMarktrolle = Column(String)
    DatumLetzteAktualisierung = Column(DateTime(timezone=True))


class MarketActors(ParentAllTables, Base):
    __tablename__ = "market_actors"

    MastrNummer = Column(String, primary_key=True)
    Personenart = Column(String)
    Marktfunktion = Column(String)
    RegistergerichtAusland = Column(String)
    Registernummer = Column(String)
    DatumLetzeAktualisierung = Column(DateTime(timezone=True))
    Firmenname = Column(String)
    Rechtsform = Column(String)
    Land = Column(String)
    Strasse = Column(String)
    Hausnummer = Column(String)
    Hausnummer_nv = Column(Boolean)
    Postleitzahl = Column(String)
    Ort = Column(String)
    Bundesland = Column(String)
    Nuts2 = Column(String)
    Email = Column(String)
    Telefon = Column(String)
    Fax_nv = Column(Boolean)
    Webseite_nv = Column(Boolean)
    Taetigkeitsbeginn = Column(Date)
    AcerCode_nv = Column(Boolean)
    Umsatzsteueridentifikationsnummer_nv = Column(Boolean)
    BundesnetzagenturBetriebsnummer = Column(String)
    BundesnetzagenturBetriebsnummer_nv = Column(Boolean)
    HausnummerAnZustelladresse_nv = Column(Boolean)
    Kmu = Column(Integer)
    RegistrierungsdatumMarktakteur = Column(DateTime(timezone=True))
    Fax = Column(String)
    HauptwirtdschaftszweigAbteilung = Column(String)
    HauptwirtdschaftszweigGruppe = Column(String)
    HauptwirtdschaftszweigAbschnitt = Column(String)
    Webseite = Column(String)
    Umsatzsteueridentifikationsnummer = Column(String)
    Registergericht = Column(String)
    Adresszusatz = Column(String)
    LandAnZustelladresse = Column(String)
    PostleitzahlAnZustelladresse = Column(String)
    OrtAnZustelladresse = Column(String)
    StrasseAnZustelladresse = Column(String)
    HausnummerAnZustelladresse = Column(String)
    RegisternummerAusland = Column(String)
    SonstigeRechtsform = Column(String)
    AcerCode = Column(String)
    AdresszusatzAnZustelladresse = Column(String)
    Taetigkeitsende = Column(Date)
    Region = Column(String)
    Taetigkeitsende_nv = Column(Boolean)
    Marktrollen = Column(String)
    Gasgrosshaendler = Column(Boolean)
    BelieferungVonLetztverbrauchernGas = Column(Boolean)
    BelieferungHaushaltskundenGas = Column(Boolean)
    Netz = Column(String)
    Direktvermarktungsunternehmen = Column(Boolean)
    BelieferungVonLetztverbrauchernStrom = Column(Boolean)
    BelieferungHaushaltskundenStrom = Column(Boolean)
    Stromgrosshaendler = Column(Boolean)
    MarktakteurVorname = Column(String)
    MarktakteurNachname = Column(String)


class Grids(ParentAllTables, Base):
    __tablename__ = "grids"

    MastrNummer = Column(String, primary_key=True)
    DatumLetzteAktualisierung = Column(DateTime(timezone=True))
    Sparte = Column(String)
    KundenAngeschlossen = Column(String)
    GeschlossenesVerteilnetz = Column(String)
    Bezeichnung = Column(String)
    Marktgebiet = Column(String)


class GridConnections(ParentAllTables, Base):
    __tablename__ = "grid_connections"

    NetzanschlusspunktMastrNummer = Column(String, primary_key=True)
    NetzanschlusspunktBezeichnung = Column(String)
    LetzteAenderung = Column(DateTime(timezone=True))
    LokationMaStRNummer = Column(String)
    Lokationtyp = Column(String)
    MaximaleEinspeiseleistung = Column(Float)
    Gasqualitaet = Column(String)
    NetzMaStRNummer = Column(String)
    NochInPlanung = Column(Boolean)
    NameDerTechnischenLokation = Column(String)
    MaximaleAusspeiseleistung = Column(Float)
    Messlokation = Column(String)
    Spannungsebene = Column(String)
    BilanzierungsgebietNetzanschlusspunktId = Column(Integer)
    Nettoengpassleistung = Column(Float)
    Netzanschlusskapazitaet = Column(Float)


tablename_mapping = {
    "anlageneegbiomasse": {
        "__name__": BiomassEeg.__tablename__,
        "__class__": BiomassEeg,
        "replace_column_names": {
            "VerknuepfteEinheitenMaStRNummern": "VerknuepfteEinheit"
        },
    },
    "einheitenbiomasse": {
        "__name__": BiomassExtended.__tablename__,
        "__class__": BiomassExtended,
        "replace_column_names": None,
    },
    "anlageneeggeosolarthermiegrubenklaerschlammdruckentspannung": {
        "__name__": GsgkEeg.__tablename__,
        "__class__": GsgkEeg,
        "replace_column_names": {
            "VerknuepfteEinheitenMaStRNummern": "VerknuepfteEinheit"
        },
    },
    "einheitengeosolarthermiegrubenklaerschlammdruckentspannung": {
        "__name__": GsgkExtended.__tablename__,
        "__class__": GsgkExtended,
        "replace_column_names": None,
    },
    "anlageneegsolar": {
        "__name__": SolarEeg.__tablename__,
        "__class__": SolarEeg,
        "replace_column_names": {
            "VerknuepfteEinheitenMaStRNummern": "VerknuepfteEinheit"
        },
    },
    "einheitensolar": {
        "__name__": SolarExtended.__tablename__,
        "__class__": SolarExtended,
        "replace_column_names": {
            "VerknuepfteEinheitenMaStRNummern": "VerknuepfteEinheit"
        },
    },
    "anlageneegspeicher": {
        "__name__": StorageEeg.__tablename__,
        "__class__": StorageEeg,
        "replace_column_names": {
            "VerknuepfteEinheitenMaStRNummern": "VerknuepfteEinheit"
        },
    },
    "anlageneegwasser": {
        "__name__": HydroEeg.__tablename__,
        "__class__": HydroEeg,
        "replace_column_names": {
            "VerknuepfteEinheitenMaStRNummern": "VerknuepfteEinheit"
        },
    },
    "einheitenwasser": {
        "__name__": HydroExtended.__tablename__,
        "__class__": HydroExtended,
        "replace_column_names": None,
    },
    "anlageneegwind": {
        "__name__": WindEeg.__tablename__,
        "__class__": WindEeg,
        "replace_column_names": {
            "VerknuepfteEinheitenMaStRNummern": "VerknuepfteEinheit"
        },
    },
    "einheitenwind": {
        "__name__": WindExtended.__tablename__,
        "__class__": WindExtended,
        "replace_column_names": None,
    },
    "anlagengasspeicher": {
        "__name__": GasStorage.__tablename__,
        "__class__": GasStorage,
        "replace_column_names": {
            "VerknuepfteEinheitenMaStRNummern": "VerknuepfteEinheit"
        },
    },
    "einheitengasspeicher": {
        "__name__": GasStorageExtended.__tablename__,
        "__class__": GasStorageExtended,
        "replace_column_names": None,
    },
    "anlagenkwk": {
        "__name__": Kwk.__tablename__,
        "__class__": Kwk,
        "replace_column_names": {
            "VerknuepfteEinheitenMaStRNummern": "VerknuepfteEinheiten"
        },
    },
    "anlagenstromspeicher": {
        "__name__": StorageUnits.__tablename__,
        "__class__": StorageUnits,
        "replace_column_names": {
            "VerknuepfteEinheitenMaStRNummern": "VerknuepfteEinheit"
        },
    },
    "bilanzierungsgebiete": {
        "__name__": BalancingArea.__tablename__,
        "__class__": BalancingArea,
        "replace_column_names": None,
    },
    "einheitengaserzeuger": {
        "__name__": GasProducer.__tablename__,
        "__class__": GasProducer,
        "replace_column_names": None,
    },
    "einheitengasverbraucher": {
        "__name__": GasConsumer.__tablename__,
        "__class__": GasConsumer,
        "replace_column_names": {
            "VerknuepfteEinheitenMaStRNummern": "VerknuepfteEinheit"
        },
    },
    "einheitengenehmigung": {
        "__name__": Permit.__tablename__,
        "__class__": Permit,
        "replace_column_names": {
            "VerknuepfteEinheitenMaStRNummern": "VerknuepfteEinheiten"
        },
    },
    "einheitenkernkraft": {
        "__name__": NuclearExtended.__tablename__,
        "__class__": NuclearExtended,
        "replace_column_names": None,
    },
    "einheitenstromverbraucher": {
        "__name__": ElectricityConsumer.__tablename__,
        "__class__": ElectricityConsumer,
        "replace_column_names": None,
    },
    "einheitenstromspeicher": {
        "__name__": StorageExtended.__tablename__,
        "__class__": StorageExtended,
        "replace_column_names": None,
    },
    "einheitenverbrennung": {
        "__name__": CombustionExtended.__tablename__,
        "__class__": CombustionExtended,
        "replace_column_names": None,
    },
    "marktrollen": {
        "__name__": MarketRoles.__tablename__,
        "__class__": MarketRoles,
        "replace_column_names": None,
    },
    "marktakteure": {
        "__name__": MarketActors.__tablename__,
        "__class__": MarketActors,
        "replace_column_names": None,
    },
    "netze": {
        "__name__": Grids.__tablename__,
        "__class__": Grids,
        "replace_column_names": None,
    },
    "netzanschlusspunkte": {
        "__name__": GridConnections.__tablename__,
        "__class__": GridConnections,
        "replace_column_names": None,
    },
    "katalogkategorien": {
        "__name__": "katalogkategorien",
        "__class__": None,
        "replace_column_names": None,
    },
    "katalogwerte": {
        "__name__": "katalogwerte",
        "__class__": None,
        "replace_column_names": None,
    },
    "lokationen": {
        "__name__": LocationExtended.__tablename__,
        "__class__": LocationExtended,
        "replace_column_names": {
            "VerknuepfteEinheitenMaStRNummern": "VerknuepfteEinheiten",
            "NetzanschlusspunkteMaStRNummern": "Netzanschlusspunkte",
        },
    },
    "einheitentypen": {
        "__name__": "einheitentypen",
        "__class__": None,
        "replace_column_names": None,
    },
}

# List of technologies which can be called by mastr.download()
#  as well as by MastrMirror.basic_backfill()
bulk_technologies = [
    "wind",
    "solar",
    "biomass",
    "hydro",
    "gsgk",
    "combustion",
    "nuclear",
    "gas",
    "storage",
    "electricity_consumer",
    "location",
    "market",
    "grid",
    "balancing_area",
    "permit",
]

# Map bulk technologies to bulk download tables
bulk_include_tables_map = {
    "wind": ["anlageneegwind", "einheitenwind"],
    "solar": ["anlageneegsolar", "einheitensolar"],
    "biomass": ["anlageneegbiomasse", "einheitenbiomasse"],
    "hydro": ["anlageneegwasser", "einheitenwasser"],
    "gsgk": [
        "anlageneeggeosolarthermiegrubenklaerschlammdruckentspannung",
        "einheitengeosolarthermiegrubenklaerschlammdruckentspannung",
    ],
    "combustion": ["anlagenkwk"],
    "nuclear": ["einheitenkernkraft"],
    "storage": ["anlageneegspeicher", "anlagenstromspeicher", "einheitenstromspeicher"],
    "gas": [
        "anlagengasspeicher",
        "einheitengaserzeuger",
        "einheitengasspeicher",
        "einheitengasverbraucher",
    ],
    "electricity_consumer": ["einheitenstromverbraucher", "einheitenverbrennung"],
    "location": ["lokationen"],
    "market": ["marktakteure", "marktrollen"],
    "grid": ["netzanschlusspunkte", "netze"],
    "balancing_area": ["bilanzierungsgebiete"],
    "permit": ["einheitengenehmigung"],
}
